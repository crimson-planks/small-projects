const { createApp, ref } = Vue
var safetext = function(text){
  //https://codereview.stackexchange.com/a/126722
	var table = {
		'<': 'lt',
		'>': 'gt',
		'"': 'quot',
		'\'': 'apos',
		'&': 'amp',
		'\r': '#10',
		'\n': '#13'
	};
	
	return text.toString().replace(/[<>"'\r\n&]/g, function(chr){
		return '&' + table[chr] + ';';
	});
}
let linkuLaDatabase = {}
async function getLinkuLaDatabase() {
  let r = await fetch("https://linku.la/jasima/data.json");
  //console.log(r.json())
  linkuLaDatabase = await (r.json())
}
getLinkuLaDatabase()
function getPuWords(){
  for(word in linkuLaDatabase.data){
    console.log(linkuLaDatabase.data[word].coined_era)
  }
}
const game={
  choiceArray: ["lon","supa","ona","pona"],
  promptString: "asdf",
  correctAnswer: 0,
  incrementingArray: (()=>{let r=Array(4);for(let i=0;i<4;i++)r[i]=i;return r})(),
  nextWordList: null
}
createApp({
    setup(){
        console.log("setup method called")
        return {
          game,
          visual: {
            choiceArray: []
          },
          loadData(){
            console.log()
            getPuWords()
          },
          Update(){
            this.game.choiceArray.forEach((value,index)=>{this.visual.choiceArray[index]=safetext(value)})
            this.visual.promptString=safetext(this.game.promptString)
          },
          updateWordList(isCorrect){
            console.log(isCorrect)
            if(isCorrect){

            }
          },
          clickMultipleChoiceButton(id){
            console.log(`${id} clicked!`)
            this.updateWordList(id==this.correctAnswer)
          }
        }
    },
    data() {
      console.log("data method called")
      console.dir(this)
      this.Update()
      return {}
    },
  }).mount('#app');