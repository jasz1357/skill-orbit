import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const API_BASE = localStorage.getItem('skill-orbit-api-base') || 'http://127.0.0.1:8000/api/v1';
const BACKEND_MODE_KEY = 'skill-orbit-use-backend';
const AUTH_TOKEN_KEY = 'skill-orbit-auth-token';
const AUTH_USER_KEY = 'skill-orbit-auth-user';
let useBackend = localStorage.getItem(BACKEND_MODE_KEY) === '1';
let authToken = localStorage.getItem(AUTH_TOKEN_KEY) || '';
let currentUser = readJson(localStorage.getItem(AUTH_USER_KEY));

// ---------------- scene ----------------
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000);

const camera = new THREE.PerspectiveCamera(38, innerWidth/innerHeight, 0.1, 2000);
camera.position.set(0, 1.4, 6.2);

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(innerWidth, innerHeight);
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.35;
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.06;
controls.rotateSpeed = 0.4;
controls.minDistance = 3.4;
controls.maxDistance = 11;
controls.enablePan = false;

// ---------------- starfield ----------------
function makeStars(count, radius){
  const g = new THREE.BufferGeometry();
  const pos = new Float32Array(count*3);
  const col = new Float32Array(count*3);
  const sz  = new Float32Array(count);
  for(let i=0;i<count;i++){
    // uniform sphere
    const u = Math.random(), v = Math.random();
    const theta = 2*Math.PI*u;
    const phi = Math.acos(2*v - 1);
    const r = radius * (0.7 + Math.random()*0.6);
    pos[i*3+0] = r*Math.sin(phi)*Math.cos(theta);
    pos[i*3+1] = r*Math.sin(phi)*Math.sin(theta);
    pos[i*3+2] = r*Math.cos(phi);
    const t = Math.random();
    // tinted whites — cool to warm
    const c = new THREE.Color().setHSL(0.55 + (Math.random()-0.5)*0.2, 0.15, 0.6 + Math.random()*0.4);
    col[i*3+0]=c.r; col[i*3+1]=c.g; col[i*3+2]=c.b;
    sz[i] = Math.random() < 0.02 ? 2.4 : 0.6 + Math.random()*0.9;
  }
  g.setAttribute('position', new THREE.BufferAttribute(pos,3));
  g.setAttribute('color', new THREE.BufferAttribute(col,3));
  g.setAttribute('size', new THREE.BufferAttribute(sz,1));
  const m = new THREE.ShaderMaterial({
    transparent: true, depthWrite: false,
    vertexShader: `
      attribute float size;
      varying vec3 vColor;
      void main(){
        vColor = color;
        vec4 mv = modelViewMatrix * vec4(position,1.0);
        gl_PointSize = size * (300.0 / -mv.z);
        gl_Position = projectionMatrix * mv;
      }`,
    fragmentShader: `
      varying vec3 vColor;
      void main(){
        vec2 c = gl_PointCoord - 0.5;
        float d = length(c);
        float a = smoothstep(0.5, 0.0, d);
        a *= smoothstep(0.5, 0.42, d) + 0.5;
        gl_FragColor = vec4(vColor, a);
      }`,
    vertexColors: true,
  });
  return new THREE.Points(g, m);
}
scene.add(makeStars(2200, 90));

// far nebulae as faint colored gradient sphere
{
  const g = new THREE.SphereGeometry(120, 32, 32);
  const m = new THREE.ShaderMaterial({
    side: THREE.BackSide,
    uniforms: { t: { value: 0 } },
    vertexShader: `varying vec3 vN; void main(){ vN = normalize(position); gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }`,
    fragmentShader: `
      varying vec3 vN;
      void main(){
        float y = vN.y * 0.5 + 0.5;
        vec3 deep = vec3(0.0,0.0,0.0);
        vec3 warm = vec3(0.10,0.06,0.02);
        vec3 cool = vec3(0.02,0.04,0.08);
        vec3 c = mix(deep, mix(cool, warm, y), 0.45);
        gl_FragColor = vec4(c, 1.0);
      }`
  });
  scene.add(new THREE.Mesh(g, m));
}

// ---------------- earth (procedural, no textures) ----------------
const EARTH_R = 1.0;

// Night-side earth — city lights, clouds, dark ocean, subtle warm rim
const earthMat = new THREE.ShaderMaterial({
  uniforms: {
    uTime:      { value: 0 },
    uSunDir:    { value: new THREE.Vector3(0.6, 0.25, 0.75).normalize() },
    uAmber:     { value: new THREE.Color('#ffb87a') },
    uOcean:     { value: new THREE.Color('#06143a') },
    uLand:      { value: new THREE.Color('#0a0e16') },
    uCamPos:    { value: new THREE.Vector3() },
  },
  vertexShader: `
    varying vec3 vWorldPos;
    varying vec3 vNormal;
    varying vec3 vObjPos;
    void main(){
      vObjPos = normalize(position);
      vNormal = normalize(normalMatrix * normal);
      vec4 wp = modelMatrix * vec4(position,1.0);
      vWorldPos = wp.xyz;
      gl_Position = projectionMatrix * viewMatrix * wp;
    }
  `,
  fragmentShader: `
    precision highp float;
    varying vec3 vWorldPos;
    varying vec3 vNormal;
    varying vec3 vObjPos;
    uniform float uTime;
    uniform vec3 uSunDir;
    uniform vec3 uAmber;
    uniform vec3 uOcean;
    uniform vec3 uLand;
    uniform vec3 uCamPos;

    float hash(vec3 p){ return fract(sin(dot(p, vec3(127.1,311.7,74.7)))*43758.5453); }
    float noise(vec3 p){
      vec3 i=floor(p), f=fract(p);
      f = f*f*(3.0-2.0*f);
      float n = mix(
        mix(mix(hash(i+vec3(0,0,0)),hash(i+vec3(1,0,0)),f.x),
            mix(hash(i+vec3(0,1,0)),hash(i+vec3(1,1,0)),f.x),f.y),
        mix(mix(hash(i+vec3(0,0,1)),hash(i+vec3(1,0,1)),f.x),
            mix(hash(i+vec3(0,1,1)),hash(i+vec3(1,1,1)),f.x),f.y), f.z);
      return n;
    }
    float fbm(vec3 p){
      float v=0.0, a=0.5;
      for(int i=0;i<6;i++){ v+=a*noise(p); p*=2.07; a*=0.5; }
      return v;
    }
    float fbmWarp(vec3 p){
      vec3 q = vec3(fbm(p), fbm(p+vec3(5.2,1.3,2.8)), fbm(p+vec3(1.7,9.2,4.4)));
      return fbm(p + 1.6*q);
    }

    void main(){
      vec3 N = normalize(vObjPos);
      // continent mask via fbm in spherical coords
      float continents = fbm(N*1.8 + 3.1);
      float detail = fbm(N*5.0);
      float landMask = smoothstep(0.50, 0.58, continents + detail*0.15);

      // city lights — concentrate on coasts
      vec3 cellP = N*26.0;
      float city = 0.0;
      float coast = 1.0 - smoothstep(0.0, 0.06, abs(continents - 0.55));
      float density = landMask * (0.45 + 0.55*coast);
      for(int i=0;i<4;i++){
        float k = float(i+1);
        float v = noise(cellP*k + float(i)*7.3);
        city += pow(smoothstep(0.84, 0.99, v), 5.0) * (0.7/k);
      }
      float spark = pow(noise(cellP*3.0 + 13.0), 18.0) * 4.0;
      city += spark * landMask;
      city *= density;
      float lat = abs(N.y);
      city *= smoothstep(0.95, 0.35, lat);

      // ocean shimmer — deep cosmic blue
      float oceanFlow = fbm(N*6.0 + vec3(uTime*0.025, 0.0, -uTime*0.02));
      vec3 oceanDeep = uOcean * 0.55;
      vec3 oceanBright = uOcean * 1.25 + vec3(0.0, 0.03, 0.08);
      vec3 oceanCol = mix(oceanDeep, oceanBright, oceanFlow);
      vec3 base = mix(oceanCol, uLand, landMask);

      float diff = max(dot(N, normalize(uSunDir)), 0.0);
      float nightFactor = smoothstep(0.25, -0.05, dot(N, normalize(uSunDir)));

      // ocean blue ambient, land near-black
      vec3 ambient = mix(vec3(0.04,0.07,0.18), vec3(0.02,0.025,0.035), landMask);
      vec3 col = ambient + base * (0.45 + 1.0*diff);
      col += uAmber * city * (0.8 + 1.8*nightFactor) * 3.2;
      vec3 V = normalize(uCamPos - vWorldPos);

      // flowing clouds
      vec3 cloudP = N*2.4 + vec3(uTime*0.012, uTime*0.004, 0.0);
      float clouds = fbmWarp(cloudP);
      float cloudMask = smoothstep(0.50, 0.78, clouds);
      float wisps = smoothstep(0.62, 0.85, fbm(N*4.5 + vec3(-uTime*0.02, 0.0, uTime*0.01)));
      col += vec3(0.10, 0.10, 0.12) * cloudMask * (0.18 + 0.7*diff);
      col += vec3(0.08, 0.08, 0.10) * wisps * (0.10 + 0.6*diff) * 0.5;
      col -= uAmber * city * cloudMask * 0.35 * nightFactor;

      // (terminator removed for cleaner deep look)
      float term = 0.0;

      // subtle deep-blue rim
      float fres = pow(1.0 - max(dot(normalize(vNormal), V), 0.0), 3.5);
      col += vec3(0.18, 0.28, 0.55) * fres * 0.22;

      gl_FragColor = vec4(col, 1.0);
    }
  `,
});

const earthGeo = new THREE.SphereGeometry(EARTH_R, 96, 96);
const earth = new THREE.Mesh(earthGeo, earthMat);
scene.add(earth);

// soft atmosphere shell — warm, very subtle (no thick blue ring)
const atmoMat = new THREE.ShaderMaterial({
  transparent: true, side: THREE.BackSide, depthWrite: false, blending: THREE.AdditiveBlending,
  uniforms: { uColor:{ value: new THREE.Color('#3a2a1a') } },
  vertexShader: `varying vec3 vN; varying vec3 vP; void main(){ vN=normalize(normalMatrix*normal); vec4 mv=modelViewMatrix*vec4(position,1.0); vP=-mv.xyz; gl_Position=projectionMatrix*mv; }`,
  fragmentShader: `
    varying vec3 vN; varying vec3 vP; uniform vec3 uColor;
    void main(){
      float i = pow(1.0 - max(dot(normalize(vN), normalize(vP)),0.0), 5.0);
      gl_FragColor = vec4(uColor*i, i*0.5);
    }`
});
const atmo = new THREE.Mesh(new THREE.SphereGeometry(EARTH_R*1.04, 64, 64), atmoMat);
scene.add(atmo);

// ---------------- orbit rings (dynamic) ----------------
// Cosmic-logic helpers for procedurally generating new rings.
// - Radius increases asteroid-belt-like (~0.42 step + slight scatter)
// - Speed follows Kepler's third law (T² ∝ r³ ⇒ ω ∝ r^(-3/2))
// - Tilt is hashed from the category id so a renamed cat keeps its plane
// - Colors cycle in OKLCH space at constant L/C, hue stepping by 47° (golden-ish)
const RING_BASE_R = 1.55;
const RING_BASE_SPEED = 0.06;
const RING_STEP = 0.42;

// Stable string hash → [0,1)
function strHash01(s){
  let h = 2166136261 >>> 0;
  for(let i=0;i<s.length;i++){ h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; }
  return (h >>> 0) / 0xffffffff;
}
function tiltFromId(id){
  const a = strHash01(id+'#x') * 2 - 1;
  const b = strHash01(id+'#y') * 2 - 1;
  const c = strHash01(id+'#z') * 2 - 1;
  // ~ ±0.85 rad on x, ±0.6 on y, ±0.25 on z (real planets are mostly low-incl)
  return [ a*0.85, b*0.6, c*0.25 ];
}
function oklchToHex(L, C, hDeg){
  // OKLCH → linear sRGB → sRGB hex (Björn Ottosson formulae)
  const h = hDeg * Math.PI / 180;
  const a_ = Math.cos(h) * C;
  const b_ = Math.sin(h) * C;
  const l_ = L + 0.3963377774 * a_ + 0.2158037573 * b_;
  const m_ = L - 0.1055613458 * a_ - 0.0638541728 * b_;
  const s_ = L - 0.0894841775 * a_ - 1.2914855480 * b_;
  const l = l_*l_*l_, m = m_*m_*m_, s = s_*s_*s_;
  let r =  4.0767416621*l - 3.3077115913*m + 0.2309699292*s;
  let g = -1.2684380046*l + 2.6097574011*m - 0.3413193965*s;
  let bl=  -0.0041960863*l - 0.7034186147*m + 1.7076147010*s;
  const lin2srgb = v => {
    v = Math.max(0, Math.min(1, v));
    return v <= 0.0031308 ? 12.92*v : 1.055*Math.pow(v, 1/2.4) - 0.055;
  };
  r = Math.round(lin2srgb(r)*255);
  g = Math.round(lin2srgb(g)*255);
  bl= Math.round(lin2srgb(bl)*255);
  const h2 = n => n.toString(16).padStart(2,'0');
  return '#' + h2(r) + h2(g) + h2(bl);
}
// Default 3 categories — AI capability oriented taxonomy
const DEFAULT_RING_DEFS = [
  { id:'craft',  label:'CREATE',   labelCn:'', color:'#ffb066', r: 1.55, tilt:[ 0.30, 0.10, 0.05], speed: 0.06 },
  { id:'theory', label:'ANALYZE',  labelCn:'', color:'#7ed6e6', r: 1.95, tilt:[-0.55, 0.40, 0.20], speed: 0.04 },
  { id:'life',   label:'AUTOMATE', labelCn:'', color:'#e69aa3', r: 2.40, tilt:[ 0.80,-0.30, 0.10], speed: 0.03 },
];

const RINGS_KEY = 'skill-orbit-rings-v2';
// one-time cleanup of legacy v1 keys (Chinese labels & seeds)
try{
  if(localStorage.getItem('skill-orbit-rings-v1') || localStorage.getItem('skill-orbit-cat-labels-v1')){
    localStorage.removeItem('skill-orbit-rings-v1');
    localStorage.removeItem('skill-orbit-cat-labels-v1');
    localStorage.removeItem('skill-orbit-v1');
  }
}catch(e){}
function loadRingDefs(){
  try{
    const raw = localStorage.getItem(RINGS_KEY);
    if(raw){
      const arr = JSON.parse(raw);
      if(Array.isArray(arr) && arr.length >= 1) return arr;
    }
  }catch(e){}
  return DEFAULT_RING_DEFS.map(d => ({ ...d }));
}
function saveRingDefs(){
  try{
    const data = RINGS.map(r => ({
      id: r.id, label: r.label, labelCn: r.labelCn,
      color: '#' + new THREE.Color(r.color).getHexString(),
      r: r.r, tilt: [r.tilt.x, r.tilt.y, r.tilt.z], speed: r.speed,
    }));
    localStorage.setItem(RINGS_KEY, JSON.stringify(data));
  }catch(e){}
}

const RINGS = [];
const ringGroups = {};

function buildRing(def){
  const cfg = {
    id: def.id,
    label: def.label || def.id.toUpperCase(),
    labelCn: def.labelCn || '',
    r: def.r,
    color: new THREE.Color(def.color),
    tilt: new THREE.Euler(def.tilt[0], def.tilt[1], def.tilt[2]),
    speed: def.speed,
  };
  const grp = new THREE.Group();
  grp.rotation.copy(cfg.tilt);
  scene.add(grp);
  ringGroups[cfg.id] = grp;

  const segs = 256;
  const pts = [];
  for(let i=0;i<=segs;i++){
    const a = i/segs * Math.PI * 2;
    pts.push(new THREE.Vector3(Math.cos(a)*cfg.r, 0, Math.sin(a)*cfg.r));
  }
  const ringGeo = new THREE.BufferGeometry().setFromPoints(pts);
  const ringMat = new THREE.LineDashedMaterial({
    color: cfg.color, transparent: true, opacity: 0.25,
    dashSize: 0.08, gapSize: 0.06, linewidth: 1
  });
  const line = new THREE.Line(ringGeo, ringMat);
  line.computeLineDistances();
  grp.add(line);

  const glowGeo = new THREE.RingGeometry(cfg.r-0.005, cfg.r+0.005, 256);
  const glowMat = new THREE.MeshBasicMaterial({ color: cfg.color, transparent:true, opacity: 0.08, side:THREE.DoubleSide, blending: THREE.AdditiveBlending, depthWrite:false });
  const glow = new THREE.Mesh(glowGeo, glowMat);
  glow.rotation.x = Math.PI/2;
  grp.add(glow);

  const hlGeo = new THREE.RingGeometry(cfg.r-0.012, cfg.r+0.012, 256);
  const hlMat = new THREE.MeshBasicMaterial({ color: cfg.color, transparent:true, opacity: 0, side:THREE.DoubleSide, blending: THREE.AdditiveBlending, depthWrite:false });
  const hl = new THREE.Mesh(hlGeo, hlMat);
  hl.rotation.x = Math.PI/2;
  grp.add(hl);

  cfg._line = line; cfg._lineMat = ringMat;
  cfg._glowMat = glowMat;
  cfg._hlMat = hlMat;
  cfg._group = grp;
  RINGS.push(cfg);
  return cfg;
}

// Build initial rings from persisted defs (or defaults)
loadRingDefs().forEach(buildRing);

// Generate a new ring def with cosmic-physics-inspired params
function generateNewRingDef(label, labelCn){
  const id = 'cat_' + Date.now().toString(36) + '_' + Math.floor(Math.random()*1e4).toString(36);
  // outer radius: step from current outermost
  const maxR = RINGS.reduce((m,r)=>Math.max(m,r.r), RING_BASE_R);
  const r = maxR + RING_STEP + (Math.random()*0.08 - 0.04);
  // Kepler: ω ∝ r^(-3/2)
  const speed = RING_BASE_SPEED * Math.pow(RING_BASE_R / r, 1.5);
  const tilt = tiltFromId(id);
  // hue cycles by 47° per ring index (golden-ratio-ish, avoids collisions)
  const hue = (200 + RINGS.length * 47) % 360;
  const color = oklchToHex(0.78, 0.13, hue);
  return { id, label: (label||'').toUpperCase() || 'NEW', labelCn: labelCn||'', color, r, tilt, speed };
}

// ---- category focus state ----
let activeCat = null; // 'craft' | 'theory' | 'life' | null
function setActiveCategory(cat){
  activeCat = (activeCat === cat) ? null : cat;
  // sync UI stat rows
  document.querySelectorAll('.panel .stat.cat').forEach(el=>{
    const c = el.dataset.cat;
    el.classList.toggle('active', activeCat === c);
    el.classList.toggle('dimmed', activeCat && activeCat !== c);
  });
}
window.__setActiveCategory = setActiveCategory;

// ---------------- stars on orbits (memory nodes) ----------------
// circular sprite texture, generated once
function spriteTex(){
  const c = document.createElement('canvas'); c.width=c.height=128;
  const ctx = c.getContext('2d');
  const g = ctx.createRadialGradient(64,64,0, 64,64,60);
  g.addColorStop(0,'rgba(255,255,255,1)');
  g.addColorStop(0.25,'rgba(255,255,255,0.9)');
  g.addColorStop(0.5,'rgba(255,255,255,0.35)');
  g.addColorStop(1,'rgba(255,255,255,0)');
  ctx.fillStyle = g; ctx.beginPath(); ctx.arc(64,64,60,0,Math.PI*2); ctx.fill();
  // cross flare
  ctx.globalAlpha = 0.6;
  ctx.fillStyle = 'rgba(255,255,255,1)';
  ctx.fillRect(63, 8, 2, 112);
  ctx.fillRect(8, 63, 112, 2);
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace;
  return t;
}
const STAR_TEX = spriteTex();

const memoryNodes = []; // { mesh, ring, angle, speed, name, cat, day, color, idx, id, note, created }

let _idCounter = 0;
function genId(){ return 'n_' + Date.now().toString(36) + '_' + (_idCounter++).toString(36); }

function addNode({ id, name, cat='craft', day=0, animateBirth=true, note='', created=Date.now(), angle, persist=true }){
  const cfg = RINGS.find(r=>r.id===cat) || RINGS[0];
  const grp = ringGroups[cfg.id];

  const mat = new THREE.SpriteMaterial({
    map: STAR_TEX,
    color: cfg.color,
    transparent: true,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  });
  const sp = new THREE.Sprite(mat);
  const baseScale = 0.16;
  sp.scale.set(baseScale, baseScale, baseScale);
  sp.userData = { isNode: true };
  grp.add(sp);

  const node = {
    id: id || genId(),
    mesh: sp,
    ring: cfg,
    angle: angle != null ? angle : Math.random() * Math.PI * 2,
    speed: cfg.speed * (0.85 + Math.random()*0.3),
    name, cat, day,
    color: cfg.color,
    twinklePhase: Math.random()*Math.PI*2,
    born: performance.now(),
    animateBirth,
    idx: memoryNodes.length + 1,
    note: note || '',
    created,
  };
  memoryNodes.push(node);
  refreshUI();
  if(persist) saveState();
  return node;
}

function removeNode(id, { sync=true } = {}){
  const i = memoryNodes.findIndex(n=>n.id===id);
  if(i<0) return;
  const n = memoryNodes[i];
  if(sync && useBackend && authToken){
    apiFetch(`/skills/${encodeURIComponent(id)}`, { method: 'DELETE' }).catch(showApiError);
  }
  if(n.mesh.parent) n.mesh.parent.remove(n.mesh);
  n.mesh.material.dispose();
  memoryNodes.splice(i,1);
  // re-index
  memoryNodes.forEach((m, k)=> m.idx = k+1);
  refreshUI();
  if(!useBackend) saveState();
}

function clearNodes(){
  memoryNodes.slice().forEach(n => removeNode(n.id, { sync:false }));
}

// ---------------- persistence ----------------
const STORE_KEY = 'skill-orbit-v2';
function saveState(){
  if(useBackend) return;
  try{
    const data = memoryNodes.map(n => ({
      id: n.id, name: n.name, cat: n.cat, note: n.note,
      created: n.created, angle: n.angle,
    }));
    localStorage.setItem(STORE_KEY, JSON.stringify(data));
  }catch(e){}
}
function loadState(){
  try{
    const raw = localStorage.getItem(STORE_KEY);
    if(!raw) return null;
    return JSON.parse(raw);
  }catch(e){ return null; }
}

function readJson(raw){
  try{ return raw ? JSON.parse(raw) : null; }catch(e){ return null; }
}

async function apiFetch(path, options={}){
  const headers = {
    'Content-Type': 'application/json',
    ...(options.headers || {}),
  };
  if(authToken) headers.Authorization = `Bearer ${authToken}`;
  const res = await fetch(`${API_BASE}${path}`, { ...options, headers });
  if(res.status === 401){
    clearAuth();
    showAuthPanel('login', 'Your session expired. Please sign in again.');
  }
  if(!res.ok){
    let message = `Request failed (${res.status})`;
    try{
      const body = await res.json();
      message = body.detail || message;
    }catch(e){}
    throw new Error(message);
  }
  if(res.status === 204) return null;
  return res.json();
}

function showApiError(err){
  appendMsg('sys', escapeHtml(err.message || 'Backend request failed.'));
}

function clearAuth(){
  authToken = '';
  currentUser = null;
  localStorage.removeItem(AUTH_TOKEN_KEY);
  localStorage.removeItem(AUTH_USER_KEY);
}

function scheduleNodeUpdate(node, patch){
  if(!useBackend || !authToken || !node) return;
  clearTimeout(node._syncT);
  node._syncT = setTimeout(()=>{
    apiFetch(`/skills/${encodeURIComponent(node.id)}`, {
      method: 'PATCH',
      body: JSON.stringify(patch),
    }).catch(showApiError);
  }, 250);
}

let pendingPanelConfirm = null;
let activePanelConfirmKind = null;
function askPanelConfirm(kind, message, onConfirm){
  closePanelConfirm(false);
  const box = document.getElementById(`${kind}-confirm`);
  const msg = document.getElementById(`${kind}-confirm-msg`);
  const ok = document.getElementById(`${kind}-confirm-ok`);
  const cancel = document.getElementById(`${kind}-confirm-cancel`);
  if(!box || !msg || !ok || !cancel){
    onConfirm();
    return;
  }
  pendingPanelConfirm = onConfirm;
  activePanelConfirmKind = kind;
  msg.textContent = message;
  box.classList.add('show');
  ok.focus();
}

function closePanelConfirm(run=false){
  const box = activePanelConfirmKind ? document.getElementById(`${activePanelConfirmKind}-confirm`) : null;
  const fn = pendingPanelConfirm;
  pendingPanelConfirm = null;
  activePanelConfirmKind = null;
  if(box) box.classList.remove('show');
  if(run && fn) fn();
}

['archive', 'node'].forEach(kind=>{
  const ok = document.getElementById(`${kind}-confirm-ok`);
  const cancel = document.getElementById(`${kind}-confirm-cancel`);
  if(ok) ok.addEventListener('click', ()=> closePanelConfirm(true));
  if(cancel) cancel.addEventListener('click', ()=> closePanelConfirm(false));
});
addEventListener('keydown', (e)=>{
  if(e.key === 'Escape' && pendingPanelConfirm) closePanelConfirm(false);
});

// ---------------- raycaster for hover ----------------
const ray = new THREE.Raycaster();
ray.params.Sprite = { threshold: 0.01 };
const mouse = new THREE.Vector2(-9, -9);
const tooltipEl = document.getElementById('tooltip');
let hovered = null;

addEventListener('pointermove', (e)=>{
  mouse.x = (e.clientX / innerWidth)*2 - 1;
  mouse.y = -(e.clientY / innerHeight)*2 + 1;
  tooltipEl.style.left = e.clientX + 'px';
  tooltipEl.style.top  = e.clientY + 'px';
});

// ---------------- UI ----------------
const $ = (s)=>document.querySelector(s);
const feedEl = $('#feed');
const inputEl = $('#input');
const sendBtn = $('#send');
const skillListEl = $('#skill-list');
const skillUl = $('#skill-ul');

function colorForCat(cat){
  const cfg = RINGS.find(r=>r.id===cat);
  if(cfg) return '#' + cfg.color.getHexString();
  return '#ffb066';
}

function renderCategoryRows(counts){
  const list = document.getElementById('cat-list');
  if(!list) return;
  // build rows for each ring in order
  list.innerHTML = RINGS.map(r => {
    const hex = '#' + r.color.getHexString();
    return `<div class="stat cat" data-cat="${r.id}" title="Click to focus the ${escapeHtml(r.label)} ring">
      <span class="k" style="color:${hex}">${escapeHtml(r.label)}</span>
      <span class="right" style="display:flex; align-items:center; gap:4px;">
        <span class="v">${String(counts[r.id]||0).padStart(2,'0')}</span>
        ${RINGS.length > 1 ? `<button class="del-cat" data-del-cat="${r.id}" aria-label="delete category" title="Delete category (its nodes move to the first remaining ring)">×</button>` : ''}
      </span>
    </div>`;
  }).join('');
  // restore active state
  list.querySelectorAll('.stat.cat').forEach(el=>{
    const c = el.dataset.cat;
    el.classList.toggle('active', activeCat === c);
    el.classList.toggle('dimmed', activeCat && activeCat !== c);
  });
}

function refreshUI(){
  const counts = {};
  memoryNodes.forEach(n => counts[n.cat] = (counts[n.cat]||0)+1 );
  setStat('stat-total', memoryNodes.length);
  renderCategoryRows(counts);
  const tc = document.getElementById('ticker-count');
  if(tc) tc.textContent = String(memoryNodes.length).padStart(2,'0');

  // skill list
  skillListEl.classList.toggle('empty', memoryNodes.length === 0);
  const q = (window.__skillQuery || '').trim().toLowerCase();
  const recent = memoryNodes.slice().reverse();
  const filtered = q ? recent.filter(n => n.name.toLowerCase().includes(q) || (n.note||'').toLowerCase().includes(q)) : recent;
  skillListEl.classList.toggle('no-results', q !== '' && filtered.length === 0);
  skillUl.innerHTML = filtered.map(n => {
    const sw = colorForCat(n.cat);
    const hasNote = n.note && n.note.trim() ? '<span class="note-dot" title="Has notes"></span>' : '';
    return `<li data-id="${n.id}">
      <span class="idx">${String(n.idx).padStart(2,'0')}</span>
      <span class="sw" style="background:${sw}; box-shadow:0 0 8px ${sw}"></span>
      <span class="nm">${highlightMatch(n.name, q)}</span>
      ${hasNote}
      <button class="del" data-del="${n.id}" aria-label="delete">×</button>
    </li>`;
  }).join('');
}
function highlightMatch(text, q){
  const safe = escapeHtml(text);
  if(!q) return safe;
  const lower = text.toLowerCase();
  let out = '';
  let i = 0;
  while(i < text.length){
    const idx = lower.indexOf(q, i);
    if(idx === -1){ out += escapeHtml(text.slice(i)); break; }
    out += escapeHtml(text.slice(i, idx));
    out += '<mark>' + escapeHtml(text.slice(idx, idx + q.length)) + '</mark>';
    i = idx + q.length;
  }
  return out;
}
function setStat(id, n){
  const el = document.getElementById(id);
  if(!el) return;
  el.querySelector('.v').textContent = String(n).padStart(2,'0');
  el.classList.add('flash');
  setTimeout(()=>el.classList.remove('flash'), 400);
}
function escapeHtml(s){
  return s.replace(/[&<>"']/g, m => ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[m]));
}

function appendMsg(who, body, opts={}){
  const div = document.createElement('div');
  div.className = `msg ${who}`;
  const whoLabel = who === 'user' ? 'YOU' : who === 'ai' ? 'ORBIT' : 'SYSTEM';
  div.innerHTML = `<div class="who">${whoLabel}</div><div class="body"></div>`;
  div.querySelector('.body').innerHTML = body;
  feedEl.appendChild(div);
  feedEl.scrollTop = feedEl.scrollHeight;
  return div;
}

// classify a skill (heuristic fallback if AI fails)
function heuristicClassify(text){
  const s = text.toLowerCase();
  // AI capability keyword sets mapped to stable category ids
  const tables = {
    craft: ['build','create','write','draft','generate','design','prototype','ui','ux','code','program','react','javascript','python','app','website'],
    theory: ['analyze','analysis','research','reason','explain','compare','evaluate','summarize','insight','metric','data','model','math','logic'],
    life: ['automate','workflow','pipeline','agent','schedule','integrate','deploy','ops','operation','process','task','script','monitor','sync']
  };
  for(const [id, words] of Object.entries(tables)){
    if(RINGS.find(r=>r.id===id) && words.some(k=>s.includes(k))) return id;
  }
  return RINGS[0] ? RINGS[0].id : 'craft';
}

async function classifyWithAI(text){
  const cats = RINGS.map(r => ({ id: r.id, label: r.label, cn: r.labelCn }));
  const validIds = cats.map(c => c.id);
  // graceful fallback if running outside the host environment (no window.claude)
  if(typeof window === 'undefined' || !window.claude || typeof window.claude.complete !== 'function'){
    return { name: text.length > 32 ? text.slice(0,32) : text, cat: heuristicClassify(text), oneLine: 'Logged to the orbit.' };
  }
  const catBlock = cats.map(c => `- ${c.id} (${c.label})`).join('\n');
  const idsLine = validIds.join('|');
  const prompt = `User said: "${text}"

Extract the specific skill/idea being learned and assign it to one of these categories:
${catBlock}

Return ONLY a JSON object, no extra prose, in exactly this shape:
{"name":"<a short skill name, 3-8 words>","cat":"${idsLine}","oneLine":"<one short encouraging sentence in English, max ~16 words, optionally hint at where to use it>"}`;
  try{
    const res = await window.claude.complete(prompt);
    const m = res.match(/\{[\s\S]*\}/);
    if(!m) throw new Error('no json');
    const parsed = JSON.parse(m[0]);
    if(!validIds.includes(parsed.cat)) parsed.cat = heuristicClassify(text);
    if(!parsed.name) parsed.name = text.slice(0, 32);
    return parsed;
  }catch(e){
    return {
      name: text.slice(0, 32),
      cat: heuristicClassify(text),
      oneLine: 'Logged to the memory orbit.'
    };
  }
}

async function handleSend(){
  if(!currentUser){
    showLoginNudge();
    return;
  }
  const text = inputEl.value.trim();
  if(!text) return;
  inputEl.value = '';
  sendBtn.disabled = true;

  appendMsg('user', escapeHtml(text));

  // typing indicator
  const ind = appendMsg('ai', '<span class="dots">parsing</span>');
  const dots = ind.querySelector('.dots');
  let d=0; const tID = setInterval(()=>{ d=(d+1)%4; dots.textContent='parsing'+'.'.repeat(d) }, 220);

  let parsed;
  let createdSkill = null;
  let comboSuggestions = [];
  let detectedIntent = 'learned_skill';
  try{
    if(useBackend){
      const data = await apiFetch('/chat/assist', {
        method: 'POST',
        body: JSON.stringify({ text }),
      });
      detectedIntent = data.intent || 'learned_skill';
      comboSuggestions = Array.isArray(data.combos) ? data.combos : [];
      if(data.category){
        ensureRingFromApi(data.category);
      }
      if(data.skill){
        createdSkill = data.skill;
        parsed = {
          name: createdSkill.name,
          cat: createdSkill.category_id,
          oneLine: data.message || 'Logged to the orbit.',
        };
      } else {
        parsed = {
          name: '',
          cat: RINGS[0] ? RINGS[0].id : 'craft',
          oneLine: data.message || 'Suggestions ready.',
        };
      }
    } else {
      parsed = await classifyWithAI(text);
    }
  }catch(err){
    clearInterval(tID);
    ind.remove();
    appendMsg('sys', escapeHtml(err.message || 'Could not reach backend.'));
    sendBtn.disabled = false;
    inputEl.focus();
    return;
  }
  clearInterval(tID);

  // remove the indicator and replace
  ind.remove();
  if(useBackend && parsed && parsed.cat && !RINGS.find(r => r.id === parsed.cat)){
    try{
      const categories = await apiFetch('/categories');
      categories.forEach(ensureRingFromApi);
    }catch(e){}
  }
  if(detectedIntent === 'goal_planning' && comboSuggestions.length){
    const combosHtml = comboSuggestions.slice(0, 3).map((combo, idx)=>{
      const skills = Array.isArray(combo.skills) ? combo.skills : [];
      const skillNames = skills.map(s => escapeHtml(s.name)).join(' + ');
      const reason = escapeHtml(combo.reason || '');
      return `<div style="margin-top:${idx===0 ? 8 : 10}px; padding-top:8px; border-top:1px solid var(--line);">
        <div style="font-size:10px; letter-spacing:.12em; color:var(--ink);">COMBO ${idx+1}</div>
        <div style="margin-top:4px; font-size:12px;">${skillNames || escapeHtml(combo.title || 'Skill combo')}</div>
        <div style="margin-top:5px; color:var(--dim); font-size:11px; line-height:1.5;">${reason}</div>
      </div>`;
    }).join('');
    appendMsg('ai', `${escapeHtml(parsed.oneLine || 'Suggestions ready.')}${combosHtml}`);
  } else {
    const cfg = RINGS.find(r=>r.id===parsed.cat);
    const catLabel = cfg ? cfg.label : parsed.cat.toUpperCase();
    const sw = colorForCat(parsed.cat);
    appendMsg('ai',
      `${escapeHtml(parsed.oneLine || 'Logged to the memory orbit.')}<br/>
       <span class="pill"><span class="sw" style="background:${sw}; box-shadow:0 0 8px ${sw}"></span> +1 NODE · <code>${catLabel}</code></span>
       <div style="margin-top:6px; color:var(--dim); font-family:JetBrains Mono,monospace; font-size:10px; letter-spacing:0.2em;">→ ${escapeHtml(parsed.name)}</div>`
    );

    if(createdSkill){
      addNode({
        id: createdSkill.id,
        name: createdSkill.name,
        cat: createdSkill.category_id,
        note: createdSkill.note || '',
        created: Date.parse(createdSkill.created_at) || Date.now(),
        angle: createdSkill.angle,
        animateBirth: true,
        persist: false,
      });
    } else {
      addNode({ name: parsed.name, cat: parsed.cat, day: 0, animateBirth: true });
    }
  }

  sendBtn.disabled = false;
  inputEl.focus();
}

sendBtn.addEventListener('click', handleSend);
inputEl.addEventListener('keydown', (e)=>{
  if(e.key === 'Enter') handleSend();
});

// click on skill list -> open detail card; or delete via × button
skillUl.addEventListener('click', (e)=>{
  const delBtn = e.target.closest('button.del');
  if(delBtn){
    e.stopPropagation();
    const id = delBtn.dataset.del;
    const n = memoryNodes.find(x=>x.id===id); if(!n) return;
    askPanelConfirm('node', '确认要删除此条技能吗？删除数据不可恢复。', ()=> flyOutAndRemove(n));
    return;
  }
  const li = e.target.closest('li'); if(!li) return;
  const id = li.dataset.id;
  const n = memoryNodes.find(x=>x.id===id); if(!n) return;
  openDetail(n);
});

function flyOutAndRemove(n){
  // brief fade-out animation
  const start = performance.now();
  const dur = 380;
  const baseS = n.mesh.scale.x;
  function step(){
    const t = Math.min(1, (performance.now()-start)/dur);
    const s = baseS * (1 - t) + 0.001;
    n.mesh.scale.set(s,s,s);
    n.mesh.material.opacity = 1 - t;
    if(t<1) requestAnimationFrame(step);
    else removeNode(n.id);
  }
  step();
}

// ---------- detail card ----------
const detailEl = document.getElementById('detail');
const detailName = document.getElementById('detail-name');
const detailMeta = document.getElementById('detail-meta');
const detailNote = document.getElementById('detail-note');
const detailSwatch = document.getElementById('detail-swatch');
let openNode = null;

function openDetail(n){
  openNode = n;
  detailName.textContent = n.name;
  const cfg = RINGS.find(r=>r.id===n.cat);
  const catName = cfg ? cfg.label : n.cat.toUpperCase();
  const catCn = cfg && cfg.labelCn ? cfg.labelCn : '';
  const catLabel = catCn ? `${catName} · ${catCn}` : catName;
  const dateStr = new Date(n.created || Date.now()).toLocaleDateString('zh-CN');
  detailMeta.innerHTML = `<span>${escapeHtml(catLabel)}</span><span class="sep">·</span><span>NODE ${String(n.idx).padStart(3,'0')}</span><span class="sep">·</span><span>${dateStr}</span>`;
  const sw = colorForCat(n.cat);
  detailSwatch.style.background = sw;
  detailSwatch.style.boxShadow = `0 0 16px ${sw}`;
  detailNote.value = n.note || '';
  detailEl.classList.add('show');
  setTimeout(()=> detailNote.focus(), 240);

  // briefly enlarge that star to show selection
  n._selected = true;
}
function closeDetail(){
  if(openNode){
    openNode.note = detailNote.value;
    openNode._selected = false;
    if(useBackend) scheduleNodeUpdate(openNode, { note: openNode.note });
    else saveState();
    refreshUI();
  }
  openNode = null;
  detailEl.classList.remove('show');
}
document.getElementById('detail-close').addEventListener('click', closeDetail);
document.getElementById('detail-delete').addEventListener('click', ()=>{
  if(!openNode) return;
  const n = openNode;
  askPanelConfirm('node', '确认要删除此条技能吗？删除数据不可恢复。', ()=>{
    closeDetail();
    flyOutAndRemove(n);
  });
});
detailNote.addEventListener('input', ()=>{
  if(!openNode) return;
  openNode.note = detailNote.value;
  // debounced save
  clearTimeout(openNode._saveT);
  openNode._saveT = setTimeout(()=>{
    if(useBackend) scheduleNodeUpdate(openNode, { note: openNode.note });
    else saveState();
  }, 400);
});
addEventListener('keydown', (e)=>{
  if(e.key === 'Escape' && openNode) closeDetail();
});

// click on canvas to open node
renderer.domElement.addEventListener('click', (e)=>{
  // use current mouse coords already tracked
  ray.setFromCamera(mouse, camera);
  const hits = ray.intersectObjects(memoryNodes.map(n=>n.mesh), false);
  if(hits.length){
    const node = memoryNodes.find(n=>n.mesh===hits[0].object);
    if(node) openDetail(node);
  }
});

// ---------- collapse toggle ----------
const recentToggle = document.getElementById('recent-toggle');
if(recentToggle){
  recentToggle.addEventListener('click', ()=>{
    skillListEl.classList.toggle('collapsed');
    recentToggle.textContent = skillListEl.classList.contains('collapsed') ? '+' : '−';
  });
}
const archiveSection = document.getElementById('archive-section');
const archiveToggle = document.getElementById('archive-toggle');
if(archiveToggle && archiveSection){
  archiveToggle.addEventListener('click', ()=>{
    archiveSection.classList.toggle('collapsed');
    archiveToggle.textContent = archiveSection.classList.contains('collapsed') ? '+' : '−';
  });
}

// ---------- recent nodes search ----------
const skillSearchEl = document.getElementById('skill-search');
const skillSearchClear = document.getElementById('skill-search-clear');
if(skillSearchEl){
  skillSearchEl.addEventListener('input', ()=>{
    const v = skillSearchEl.value;
    window.__skillQuery = v;
    skillListEl.classList.toggle('has-query', v.length > 0);
    refreshUI();
  });
  skillSearchEl.addEventListener('keydown', (e)=>{
    if(e.key === 'Escape'){
      skillSearchEl.value = '';
      window.__skillQuery = '';
      skillListEl.classList.remove('has-query');
      refreshUI();
      skillSearchEl.blur();
    }
  });
}
if(skillSearchClear){
  skillSearchClear.addEventListener('click', ()=>{
    skillSearchEl.value = '';
    window.__skillQuery = '';
    skillListEl.classList.remove('has-query');
    refreshUI();
    skillSearchEl.focus();
  });
}

// ---------- chat collapse toggle ----------
const chatEl = document.getElementById('chat');
const chatToggle = document.getElementById('chat-toggle');
if(chatToggle && chatEl){
  // restore persisted state
  try{
    if(localStorage.getItem('chatCollapsed') === '1'){
      chatEl.classList.add('collapsed');
      chatToggle.textContent = '+';
    }
  }catch(e){}
  chatToggle.addEventListener('click', ()=>{
    chatEl.classList.toggle('collapsed');
    const isCollapsed = chatEl.classList.contains('collapsed');
    chatToggle.textContent = isCollapsed ? '+' : '−';
    try{ localStorage.setItem('chatCollapsed', isCollapsed ? '1' : '0'); }catch(e){}
  });
}

// ---------- category list: click/dblclick/rename + add/delete via delegation ----------
(function(){
  const list = document.getElementById('cat-list');
  if(!list) return;
  const catClickTimer = { id: null };

  list.addEventListener('click', (e)=>{
    const delBtn = e.target.closest('[data-del-cat]');
    if(delBtn){
      e.stopPropagation();
      const cat = delBtn.dataset.delCat;
      askPanelConfirm('archive', '确认要删除这条archive 吗，删除时同时删除node，数据不可恢复；', ()=> deleteCategory(cat));
      return;
    }
    const row = e.target.closest('.stat.cat'); if(!row) return;
    const k = row.querySelector('.k');
    if(k && k.isContentEditable) return;
    if(catClickTimer.id) return;
    catClickTimer.id = setTimeout(()=>{
      catClickTimer.id = null;
      const cat = row.dataset.cat;
      if(typeof window.__setActiveCategory === 'function') window.__setActiveCategory(cat);
    }, 220);
  });

  list.addEventListener('dblclick', (e)=>{
    const row = e.target.closest('.stat.cat'); if(!row) return;
    if(catClickTimer.id){ clearTimeout(catClickTimer.id); catClickTimer.id = null; }
    e.preventDefault();
    const k = row.querySelector('.k'); if(!k) return;
    k.setAttribute('contenteditable', 'true');
    k.focus();
    const range = document.createRange();
    range.selectNodeContents(k);
    const sel = window.getSelection();
    sel.removeAllRanges(); sel.addRange(range);

    const cleanup = ()=>{
      k.removeEventListener('blur', onBlur);
      k.removeEventListener('keydown', onKey);
    };
    const commit = (cancel)=>{
      const cat = row.dataset.cat;
      const cfg = RINGS.find(r=>r.id===cat);
      k.removeAttribute('contenteditable');
      if(!cancel && cfg){
        const txt = (k.textContent || '').trim().toUpperCase();
        if(txt){
          cfg.label = txt;
          if(useBackend && authToken){
            apiFetch(`/categories/${encodeURIComponent(cat)}`, {
              method: 'PATCH',
              body: JSON.stringify({ label: txt }),
            }).catch(showApiError);
          }
        }
        saveRingDefs();
      }
      cleanup();
      refreshUI();
      if(typeof openNode !== 'undefined' && openNode && detailEl.classList.contains('show')) openDetail(openNode);
    };
    const onBlur = ()=> commit(false);
    const onKey = (ev)=>{
      if(ev.key === 'Enter'){ ev.preventDefault(); commit(false); }
      if(ev.key === 'Escape'){ ev.preventDefault(); commit(true); }
    };
    k.addEventListener('blur', onBlur);
    k.addEventListener('keydown', onKey);
  });
})();

// ---------- delete category ----------
function deleteCategory(catId){
  if(RINGS.length <= 1){ alert('Keep at least one category.'); return; }
  const cfg = RINGS.find(r=>r.id===catId); if(!cfg) return;
  memoryNodes.filter(n=>n.cat===catId).forEach(n => removeNode(n.id));
  // remove ring visuals
  if(cfg._group){
    cfg._group.children.slice().forEach(ch => {
      cfg._group.remove(ch);
      if(ch.geometry) ch.geometry.dispose();
      if(ch.material) ch.material.dispose();
    });
    if(cfg._group.parent) cfg._group.parent.remove(cfg._group);
  }
  if(ringGroups[catId]) delete ringGroups[catId];
  const idx = RINGS.indexOf(cfg);
  if(idx >= 0) RINGS.splice(idx, 1);
  if(activeCat === catId) activeCat = null;
  saveRingDefs();
  saveState();
  if(useBackend && authToken){
    apiFetch(`/categories/${encodeURIComponent(catId)}`, { method: 'DELETE' }).catch(showApiError);
  }
  refreshUI();
}

// ---------- add new category ----------
(function(){
  const btn = document.getElementById('add-cat');
  const wrap = document.getElementById('add-cat-input');
  const input = document.getElementById('add-cat-name');
  if(!btn || !wrap || !input) return;
  let cancelTimer = null;
  btn.addEventListener('click', ()=>{
    if(!currentUser){
      showLoginNudge();
      return;
    }
    btn.classList.add('editing');
    wrap.classList.add('show');
    input.value = '';
    input.focus();
  });
  const cancel = ()=>{
    btn.classList.remove('editing');
    wrap.classList.remove('show');
    input.value = '';
  };
  const commit = ()=>{
    const raw = input.value.trim();
    if(!raw){ cancel(); return; }
    let label = raw, labelCn = '';
    const m = raw.match(/^(.+?)\s*[·•\-—|/]\s*(.+)$/);
    if(m){ label = m[1].trim(); labelCn = m[2].trim(); }
    label = label.toUpperCase();
    const def = generateNewRingDef(label, labelCn);
    buildRing(def);
    saveRingDefs();
    if(useBackend && authToken){
      apiFetch('/categories', {
        method: 'POST',
        body: JSON.stringify({
          id: def.id,
          label: def.label,
          label_cn: def.labelCn || '',
          color: def.color,
          radius: def.r,
          tilt: def.tilt,
          speed: def.speed,
        }),
      }).catch(showApiError);
    }
    cancel();
    refreshUI();
  };
  input.addEventListener('keydown', (e)=>{
    if(e.key === 'Enter'){ e.preventDefault(); commit(); }
    if(e.key === 'Escape'){ e.preventDefault(); cancel(); }
  });
  input.addEventListener('blur', ()=>{
    cancelTimer = setTimeout(()=>{ if(document.activeElement !== input) cancel(); }, 120);
  });
  input.addEventListener('focus', ()=>{ if(cancelTimer){ clearTimeout(cancelTimer); cancelTimer = null; } });
})();

// ---------- node name editing in detail dialog ----------
(function(){
  const nameEl = document.getElementById('detail-name');
  if(!nameEl) return;
  const commitName = ()=>{
    if(!openNode) return;
    const v = (nameEl.textContent || '').trim();
    if(v && v !== openNode.name){
      openNode.name = v;
      if(useBackend) scheduleNodeUpdate(openNode, { name: v });
      else saveState();
      refreshUI();
    } else {
      nameEl.textContent = openNode.name;
    }
  };
  nameEl.addEventListener('blur', commitName);
  nameEl.addEventListener('keydown', (e)=>{
    if(e.key === 'Enter'){ e.preventDefault(); nameEl.blur(); }
    if(e.key === 'Escape'){
      e.preventDefault();
      if(openNode) nameEl.textContent = openNode.name;
      nameEl.blur();
    }
  });
  // prevent newlines on paste
  nameEl.addEventListener('paste', (e)=>{
    e.preventDefault();
    const t = (e.clipboardData || window.clipboardData).getData('text').replace(/\s+/g, ' ').trim();
    document.execCommand('insertText', false, t);
  });
})();

// ---------------- auth + boot data ----------------
function setupAuthUI(){
  const pop = document.getElementById('auth-pop');
  const msg = document.getElementById('auth-message');
  const loginTab = document.getElementById('auth-login-tab');
  const registerTab = document.getElementById('auth-register-tab');
  const loginForm = document.getElementById('auth-login-form');
  const registerForm = document.getElementById('auth-register-form');
  const localBtn = document.getElementById('auth-local-mode');
  const loginOpen = document.getElementById('auth-login-open');
  const registerOpen = document.getElementById('auth-register-open');
  const logoutBtn = document.getElementById('auth-logout');
  const nudgeOpen = document.getElementById('login-nudge-open');
  if(!pop) return;

  const setTab = (mode)=>{
    const login = mode === 'login';
    loginTab.classList.toggle('active', login);
    registerTab.classList.toggle('active', !login);
    loginForm.classList.toggle('active', login);
    registerForm.classList.toggle('active', !login);
    msg.textContent = '';
  };
  loginTab.addEventListener('click', ()=>setTab('login'));
  registerTab.addEventListener('click', ()=>setTab('register'));

  loginForm.addEventListener('submit', async (e)=>{
    e.preventDefault();
    msg.textContent = 'Signing in...';
    try{
      const data = await apiFetch('/auth/login', {
        method: 'POST',
        body: JSON.stringify({
          username: document.getElementById('auth-login-user').value.trim(),
          password: document.getElementById('auth-login-pass').value,
        }),
      });
      await enterBackendSession(data);
    }catch(err){
      msg.textContent = err.message || 'Login failed.';
    }
  });

  registerForm.addEventListener('submit', async (e)=>{
    e.preventDefault();
    msg.textContent = 'Creating account...';
    try{
      const data = await apiFetch('/auth/register', {
        method: 'POST',
        body: JSON.stringify({
          username: document.getElementById('auth-register-user').value.trim(),
          email: document.getElementById('auth-register-email').value.trim(),
          password: document.getElementById('auth-register-pass').value,
        }),
      });
      await enterBackendSession(data);
    }catch(err){
      msg.textContent = err.message || 'Registration failed.';
    }
  });

  localBtn.addEventListener('click', ()=>{
    useBackend = false;
    localStorage.setItem(BACKEND_MODE_KEY, '0');
    clearAuth();
    pop.classList.remove('show');
    updateAuthStatus();
    loadLocalData();
  });

  loginOpen.addEventListener('click', ()=> showAuthPanel('login'));
  registerOpen.addEventListener('click', ()=> showAuthPanel('register'));
  if(nudgeOpen) nudgeOpen.addEventListener('click', ()=> showAuthPanel('login'));

  logoutBtn.addEventListener('click', ()=>{
    clearAuth();
    useBackend = false;
    localStorage.setItem(BACKEND_MODE_KEY, '0');
    showLoginNudge('Signed out. 请登陆以获得完整账户权限以及福利');
    clearNodes();
    updateAuthStatus();
    loadLocalData();
  });
}

function showAuthPanel(mode='login', message=''){
  const pop = document.getElementById('auth-pop');
  const msg = document.getElementById('auth-message');
  const loginTab = document.getElementById('auth-login-tab');
  const registerTab = document.getElementById('auth-register-tab');
  const loginForm = document.getElementById('auth-login-form');
  const registerForm = document.getElementById('auth-register-form');
  const login = mode === 'login';
  loginTab.classList.toggle('active', login);
  registerTab.classList.toggle('active', !login);
  loginForm.classList.toggle('active', login);
  registerForm.classList.toggle('active', !login);
  if(pop) pop.classList.add('show');
  if(msg) msg.textContent = message;
}

function hideAuthPanel(){
  const pop = document.getElementById('auth-pop');
  if(pop) pop.classList.remove('show');
}

let loginNudgeTimer = null;
function showLoginNudge(message='请登陆以获得完整账户权限以及福利'){
  if(currentUser) return;
  const nudge = document.getElementById('login-nudge');
  if(!nudge) return;
  nudge.querySelector('div').textContent = message;
  nudge.classList.add('show');
  clearTimeout(loginNudgeTimer);
  loginNudgeTimer = setTimeout(()=> nudge.classList.remove('show'), 4200);
}

function updateAuthStatus(){
  const text = document.getElementById('auth-status-text');
  const logout = document.getElementById('auth-logout');
  const loginOpen = document.getElementById('auth-login-open');
  const registerOpen = document.getElementById('auth-register-open');
  if(!text || !logout || !loginOpen || !registerOpen) return;
  if(useBackend && currentUser){
    text.textContent = `USER · ${currentUser.username}`;
    logout.style.display = '';
    loginOpen.style.display = 'none';
    registerOpen.style.display = 'none';
  } else {
    text.textContent = 'GUEST';
    logout.style.display = 'none';
    loginOpen.style.display = '';
    registerOpen.style.display = '';
  }
}

async function enterBackendSession(data){
  authToken = data.access_token;
  currentUser = data.user;
  useBackend = true;
  localStorage.setItem(BACKEND_MODE_KEY, '1');
  localStorage.setItem(AUTH_TOKEN_KEY, authToken);
  localStorage.setItem(AUTH_USER_KEY, JSON.stringify(currentUser));
  hideAuthPanel();
  updateAuthStatus();
  await loadBackendData();
}

async function bootData(){
  setupAuthUI();
  updateAuthStatus();
  if(useBackend){
    if(authToken){
      try{
        currentUser = await apiFetch('/auth/me');
        localStorage.setItem(AUTH_USER_KEY, JSON.stringify(currentUser));
        hideAuthPanel();
        updateAuthStatus();
        await loadBackendData();
        return;
      }catch(e){}
    }
    useBackend = false;
    localStorage.setItem(BACKEND_MODE_KEY, '0');
    updateAuthStatus();
  }
  loadLocalData();
}

function loadLocalData(){
  clearNodes();
  const saved = loadState();
  if(saved && Array.isArray(saved) && saved.length){
    saved.forEach(s => addNode({
      id: s.id, name: s.name, cat: s.cat, note: s.note || '',
      created: s.created || Date.now(), angle: s.angle, animateBirth: false, persist: false
    }));
  } else {
    try{
      const seed = JSON.parse(document.getElementById('seed-skills').textContent);
      seed.forEach(s => addNode({ name: s.name, cat: s.cat, day: s.day, animateBirth: false, persist: false }));
      saveState();
    }catch(e){}
  }
}

async function loadBackendData(){
  clearNodes();
  const categories = await apiFetch('/categories');
  categories.forEach(ensureRingFromApi);
  const skills = await apiFetch('/skills');
  skills.slice().reverse().forEach(s => addNode({
    id: s.id,
    name: s.name,
    cat: s.category_id,
    note: s.note || '',
    created: Date.parse(s.created_at) || Date.now(),
    angle: s.angle,
    animateBirth: false,
    persist: false,
  }));
  appendMsg('sys', `Backend connected as <code>${escapeHtml(currentUser.username)}</code>.`);
}

function ensureRingFromApi(category){
  const existing = RINGS.find(r => r.id === category.id);
  if(existing) return existing;
  return buildRing({
    id: category.id,
    label: category.label,
    labelCn: category.label_cn || '',
    color: category.color,
    r: category.radius,
    tilt: category.tilt,
    speed: category.speed,
  });
}

bootData();

// ---------------- HUD live values ----------------
function pad(n,l=2){ return String(n).padStart(l,'0') }
function tickHud(){
  const d = new Date();
  document.getElementById('hud-utc').textContent =
    `${pad(d.getUTCHours())}:${pad(d.getUTCMinutes())}:${pad(d.getUTCSeconds())}`;
  // pseudo lat/lon based on camera
  const e = new THREE.Euler().setFromQuaternion(camera.quaternion, 'YXZ');
  const lat = THREE.MathUtils.radToDeg(-e.x);
  const lon = THREE.MathUtils.radToDeg(-e.y);
  document.getElementById('hud-lat').textContent = `${lat>=0?'+':''}${lat.toFixed(2)}°`;
  document.getElementById('hud-lon').textContent = `${lon>=0?'+':''}${lon.toFixed(2)}°`;
}
setInterval(tickHud, 250); tickHud();

// ---------------- resize ----------------
addEventListener('resize', ()=>{
  camera.aspect = innerWidth/innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});

// ---------------- animate ----------------
let last = performance.now();
function animate(now){
  const dt = Math.min(0.05, (now - last)/1000); last = now;
  controls.update();

  earthMat.uniforms.uTime.value = now * 0.001;
  earthMat.uniforms.uCamPos.value.copy(camera.position);

  // earth slow rotation
  earth.rotation.y += dt * 0.04;
  atmo.rotation.y = earth.rotation.y;

  // animate ring opacity toward target based on activeCat
  for(const cfg of RINGS){
    const isActive = activeCat === cfg.id;
    const isOther  = activeCat && !isActive;
    const targLine = isActive ? 0.85 : isOther ? 0.06 : 0.25;
    const targGlow = isActive ? 0.35 : isOther ? 0.02 : 0.08;
    const targHl   = isActive ? 0.55 : 0.0;
    const k = 1 - Math.pow(0.001, dt); // smooth lerp
    cfg._lineMat.opacity += (targLine - cfg._lineMat.opacity) * k;
    cfg._glowMat.opacity += (targGlow - cfg._glowMat.opacity) * k;
    cfg._hlMat.opacity   += (targHl   - cfg._hlMat.opacity)   * k;
  }

  // animate nodes
  for(const n of memoryNodes){
    n.angle += n.speed * dt;
    const r = n.ring.r;
    const x = Math.cos(n.angle) * r;
    const z = Math.sin(n.angle) * r;
    // tiny vertical wobble for life
    const y = Math.sin(n.angle*3 + n.twinklePhase) * 0.012;
    n.mesh.position.set(x, y, z);

    // twinkle scale
    const tw = 0.85 + 0.25*Math.sin(now*0.005 + n.twinklePhase);
    let s = 0.16 * tw;
    if(n._selected) s = 0.32 * (0.9 + 0.15*Math.sin(now*0.012));

    // category focus: boost active cat nodes, dim others
    let targetOpacity = 1.0;
    if(activeCat){
      if(n.cat === activeCat){ s *= 1.35; targetOpacity = 1.0; }
      else { s *= 0.6; targetOpacity = 0.18; }
    }

    // birth animation
    if(n.animateBirth){
      const age = (now - n.born)/1000;
      if(age < 1.6){
        const k = age/1.6;
        s = 0.16 * tw * (1 + (1-k) * 2.0);
        n.mesh.material.opacity = 1.0;
      } else {
        n.animateBirth = false;
      }
    } else {
      const km = 1 - Math.pow(0.001, dt);
      n.mesh.material.opacity += (targetOpacity - n.mesh.material.opacity) * km;
    }

    n.mesh.scale.set(s, s, s);
  }

  // hover detection (sprites only)
  ray.setFromCamera(mouse, camera);
  const hits = ray.intersectObjects(memoryNodes.map(n=>n.mesh), false);
  if(hits.length){
    const h = hits[0].object;
    const node = memoryNodes.find(n=>n.mesh===h);
    if(node){
      hovered = node;
      tooltipEl.classList.add('show');
      document.getElementById('tt-name').textContent = node.name;
      document.getElementById('tt-meta').textContent =
        `${node.cat.toUpperCase()} · NODE ${String(node.idx).padStart(3,'0')}`;
      document.body.style.cursor = 'pointer';
    }
  } else {
    if(hovered){ tooltipEl.classList.remove('show'); document.body.style.cursor=''; hovered = null; }
  }

  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
requestAnimationFrame(animate);

// ---------------- boot fade ----------------
setTimeout(()=>{ document.getElementById('boot').classList.add('gone'); }, 700);
