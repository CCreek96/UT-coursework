
if (doc1array.length == doc2array.length){
    counter=0
    for (let i = 0; i< docarray.length; i++) {
        if (doc1array[i] =! doc2array[i]){
            counter=+1;}  
     }
     Score = counter/doc1array.length
} else {
    console.log("Incorrect format please try again")
}
 
--------------------
//docx file reader
<script src="build/docxgen.js"></script>
<script src="vendor/FileSaver.min.js"></script>
<script src="vendor/jszip-utils.js"></script>
<script>
    var loadFile=function(url,callback){
        JSZipUtils.getBinaryContent(url,callback);
    }
    loadFile("/Users/carlosalvarado/Documents/testfile.docx",function(err,content){
        var doc=new Docxgen(content);
        text=doc.getFullText();
        console.log(text);
    });
</script>

// txt file reader
function readTextFile(file) {
  var rawFile = new XMLHttpRequest();
  rawFile.open("GET", "testing.txt", true);
  rawFile.onreadystatechange = function() {
    if (rawFile.readyState === 4) {
      if(rawFile.status === 200 || rawFile.status == 0){
        var allText = rawFile.responseText;
        document.getElementById("textSection").innerHTML = allText;
    }
  }
  rawFile.send(null);
}
-----------------------------