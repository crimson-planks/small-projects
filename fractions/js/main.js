let denominator = 1, numerator = 1;
function gcdF(a,b){
    if(b==0) return a;
    return gcdF(b, a%b);
}
function reduceFraction(){
    let gcd = gcdF(numerator,denominator);
    if(gcd!=1){
        numerator/=gcd;
        denominator/=gcd;
        document.getElementById("numerator").innerHTML=numerator.toString();
        document.getElementById("denominator").innerHTML=denominator.toString();
    }
}
function updateNumerator(){
    numerator++;
    reduceFraction();
    document.getElementById("numerator").innerHTML=numerator.toString();
}
function updateDenominator(){
    denominator++;
    reduceFraction();
    document.getElementById("denominator").innerHTML=denominator.toString();
}