const currentRankSelector = document.querySelector('.character.personal_rank.selector');
const characterId = document.querySelector('.characterId').textContent;
const weaponLevel = document.querySelector('.weapon.level.selector');
const characterLevel = document.querySelector('.character.level.selector');
const warpEffectsNames = document.querySelectorAll('.warp.effect');
const warpEffectsLevels = document.querySelectorAll('.warp.level.selector');

function storeWarpEffectsLevels(){
    let warpEffectsLevelsArray = [];
    for (let i=0; i < warpEffectsLevels.length; i++){
        warpEffectsLevelsArray.push(warpEffectsLevels[i].value);
    }
    localStorage.setItem('warpEffectsLevels'+characterId, JSON.stringify(warpEffectsLevelsArray));
}

function loadWarpEffectsLevels(){
    const savedWarpEffectsLevels = JSON.parse(localStorage.getItem('warpEffectsLevels'+characterId));
    if (savedWarpEffectsLevels){
        for (let i=0; i < warpEffectsLevels.length; i++){
            warpEffectsLevels[i].value = savedWarpEffectsLevels[i];
        }
    }
}

warpEffectsLevels.forEach((elem) => {
    elem.addEventListener('input', () => {
        storeWarpEffectsLevels();
    }
    );
});

function storeWarpEffectsNames(){
    let warpEffectsNamesArray = [];
    for (let i=0; i < warpEffectsNames.length; i++){
        warpEffectsNamesArray.push(warpEffectsNames[i].value);
    }
    localStorage.setItem('warpEffectsNames'+characterId, JSON.stringify(warpEffectsNamesArray));
}

function loadWarpEffectsNames(){
    const savedWarpEffectsNames = JSON.parse(localStorage.getItem('warpEffectsNames'+characterId));
    if (savedWarpEffectsNames){
        for (let i=0; i < warpEffectsNames.length; i++){
            warpEffectsNames[i].value = savedWarpEffectsNames[i];
        }
    }
}

warpEffectsNames.forEach((elem) => {
    elem.addEventListener('input', () => {
        storeWarpEffectsNames();
    }
    );
});

function storeCharacterLevel(){
    const level = characterLevel.value;
    localStorage.setItem('characterLevel'+characterId, level);
}

function loadCharacterLevel(){
    const savedLevel = localStorage.getItem('characterLevel'+characterId);
    if (savedLevel){
        characterLevel.value = savedLevel;
    }
}

characterLevel.addEventListener('input', () => {
    storeCharacterLevel();
});

function storeWeaponLevel(){
    const level = weaponLevel.value;
    localStorage.setItem('weaponLevel'+characterId, level);
}
function loadWeaponLevel(){
    const savedLevel = localStorage.getItem('weaponLevel'+characterId);
    if (savedLevel){
        weaponLevel.value = savedLevel;
    }
}
weaponLevel.addEventListener('input', () => {
    storeWeaponLevel();
});

function loadRank(){
    const savedRank = localStorage.getItem('rank'+characterId); 
    if (savedRank){
        currentRankSelector.value = savedRank; 
    } else {
        const initialRank = document.querySelector('.character.rank').textContent;
        currentRankSelector.value = initialRank;
    }
}

function storeRank(elem){
    const rank = elem.value;
    localStorage.setItem('rank'+characterId, rank);
}

currentRankSelector.addEventListener('input', (e) => {
    storeRank(e.target);
});

function loadSkillsLevels(){
    const savedSkillsLevels = JSON.parse(localStorage.getItem('skillsLevels'+characterId));
    if (savedSkillsLevels){
        const skillsLevels = document.querySelectorAll('.skill.level.selector');
        for (let i=0; i < skillsLevels.length; i++){
            skillsLevels[i].value = savedSkillsLevels[i];
        }
    }
}

const skillsLevels = document.querySelectorAll('.skill.level.selector');
function storeSkillsLevels(){
    let skillsLevelsArray = [];
    for (let i=0; i < skillsLevels.length; i++){
        skillsLevelsArray.push(skillsLevels[i].value);
    }
    localStorage.setItem('skillsLevels'+characterId, JSON.stringify(skillsLevelsArray));
}


for (let i=0; i < skillsLevels.length; i++){
    skillsLevels[i].addEventListener('input', () => {
        storeSkillsLevels();
    });
}


const sigilsLevels = document.querySelectorAll('.sigil.level.selector');

function storeSigilsLevel(){
    let sigilsLevelsArray = [];
    for (let i=0; i < sigilsLevels.length; i++){
        sigilsLevelsArray.push(sigilsLevels[i].value);
    }
    localStorage.setItem('sigilsLevels'+characterId, JSON.stringify(sigilsLevelsArray));
}

function loadSigilsLevels(){
    const savedSigilsLevels = JSON.parse(localStorage.getItem('sigilsLevels'+characterId));
    if (savedSigilsLevels){
        for (let i=0; i < sigilsLevels.length; i++){
            sigilsLevels[i].value = savedSigilsLevels[i];
        }
    }
}

sigilsLevels.forEach((elem) => {
    elem.addEventListener('input', () => {
        storeSigilsLevel();
    });
});

function loadData(){
    loadRank();
    loadSkillsLevels();
    loadSigilsLevels();
    loadWeaponLevel();
    loadCharacterLevel();
    loadWarpEffectsNames();
    loadWarpEffectsLevels();
}
loadData();

//TODO: LOAD WARP EFFECT LEVELS AND NAMES FROM LOCAL STORAGE