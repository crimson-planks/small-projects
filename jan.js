/**
 * @param {unknown[]} a 
 * @param {unknown[]} b 
 */
function isArrayEqual(a,b){
    if(!Array.isArray(a) || !Array.isArray(b)) throw new TypeError("arguments are not array");
    if(a.length!==b.length) return false;
    for(let i=0;i<a.length;i++){
        if(a[i]!==b[i]) return false;
    }
    return true;
}
function flooredModulo(a,n){
  const q = Math.floor(a/n);
  const r = a - q*n;
  return r;
}
const youtubeIdCharArr = Array(10).fill(0).map((v,i)=>String.fromCodePoint(i+0x30)).concat(Array(26).fill(0).map((v,i)=>String.fromCodePoint(i+0x41))).concat(Array(26).fill(0).map((v,i)=>String.fromCodePoint(i+0x61))).concat(['-','_']);
/**
 * @param {string} id 
 */
function youtubeIdToIndexes(id){
  /** @type number[] */
  const rslt = [];
  for(let i=0;i<id.length;i++){
    let index = youtubeIdCharArr.findIndex((v)=>v===id[i]);
    if(index===-1) throw RangeError(`ill-formed YouTube id character: ${id[i]}`);
    rslt.push(index);
  }
  return rslt;
}
/**
 * @param {number[]} youtubeIdIndexes 
 * @param {number[]} hashArr
 */
function getOffset(youtubeIdIndexes,hashArr){
  //if(youtubeIdIndexes.length!==hashArr.length) throw TypeError("length not equal");
  /** @type number[] */
  const offset = [];
  for(let i=0;i<youtubeIdIndexes.length;i++){
    const o = youtubeIdIndexes[i]-hashArr[i];
    const r = flooredModulo(o,64);
    offset.push(r);
  }
  return offset;
}
const offsetArr = Object.freeze([60,3,54,18,31,36,7,26,8,12,43]);

const salt = Object.freeze([
  223,184,144,216,59,224,194,177,
  39,28,49,73,13,144,187,208,
  204,142,251,217,87,78,113,65,
  35,147,236,230,183,142,208,63,
  140,51,58,132,143,94,68,187,
  185,226,113,195,205,251,241,159,
  144,208,241,152,248,111,195,116,
  46,81,152,188,221,151,169,37,
  77,38,116,140,35,13,95,9,
  65,188,45,207,45,71,56,107,
  218,122,98,194,63,60,199,17,
  207,243,240,43,30,37,236,150,
  13,175,131,127,128,179,206,118,
  162,178,233,177,172,208,118,170,
  15,85,56,33,174,136,80,94,
  180,99,220,152,1,207,5,170
]);
const saltStr = salt.map((x)=>String.fromCodePoint(x)).join('');
const solutionArr = Object.freeze([190,252,40,163,108,69,145,174,152,245,122,195,115,130,147,113,61,178,138,190,101,21,8,164,171,250,213,84,224,147,99,25]);

const salt2 = Object.freeze([
  146,31,34,133,230,168,190,127,
  56,200,210,78,255,1,214,94,
  182,29,56,163,99,4,113,221,
  194,63,149,254,179,173,103,187,
  159,184,48,173,185,19,254,158,
  129,86,107,239,43,250,114,150,
  96,164,12,219,142,78,206,107,
  68,8,100,128,69,170,115,99,
  21,151,108,176,148,30,174,100,
  204,9,94,229,204,252,30,59,
  100,91,202,254,82,251,236,39,
  225,80,128,191,11,221,182,41,
  187,0,80,138,166,149,109,12,
  29,178,152,228,222,224,22,252,
  133,50,186,188,216,131,141,132,
  211,254,175,60,77,228,110,100,
]);
const salt2Str = salt2.map((x)=>String.fromCodePoint(x)).join('');
function main(){
    const attentionInput = document.getElementById("attention-input")
    const hash = sha512.sha512_256.update("");
    hash.update(saltStr);
    const hash2 = sha512.sha512_256.update("");
    hash2.update(salt2Str);
    const videoLinkAnchorElement = document.getElementById("video-link");
    if(!(videoLinkAnchorElement instanceof HTMLAnchorElement)){
      alert("Please refresh.");
      return;
    }
    attentionInput.addEventListener('change',(event)=>{
        if(!(attentionInput instanceof HTMLInputElement)) return;
        const upstr = attentionInput.value.toUpperCase();
        /** @type number[] */
        const hasharray = hash.clone().update(upstr).digest()
        if(isArrayEqual(hasharray,solutionArr)){
            console.log('solution')
            const hash2array = hash2.clone().update(upstr).digest();
            const youtubeIdStrBuilder = [];
            const youtubeIdIndexes = [];
            for(let i=0;i<11;i++){
              const o = hash2array[i]+offsetArr[i];
              const r = flooredModulo(o,64);
              youtubeIdIndexes.push(r)
              youtubeIdStrBuilder.push(youtubeIdCharArr[r])
            }
            const youtubeId = youtubeIdStrBuilder.join('');

            videoLinkAnchorElement.setAttribute("href",`https://www.youtube.com/watch?v=${youtubeId}`);
            videoLinkAnchorElement.textContent = 'Click to watch reward video (YouTube link)'
        }
    });
}

main();