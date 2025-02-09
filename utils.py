def create_test_html(options_str, file_name):
    with open(file_name, "w") as f:
        f.write("<!DOCTYPE html>"+"\n")
        f.write("<head>"+"\n")
        f.write("    <title>Visualizer</title>"+"\n")
        f.write("    <script type='text/javascript' src='puzzleGen.min.js'></script>"+"\n")
        f.write("    <script srt='jquery-3.7.1.min.js'></script>"+"\n")
        f.write("</head>"+"\n")
        f.write("<body>"+"\n")
        f.write("</body>"+"\n")
        f.write("<script>"+"\n")
        f.write("    var options_test = "+options_str+";"+"\n")
        f.write("    puzzleGen.PNG(document.body, puzzleGen.Type.CUBE, options_test);"+"\n")
        f.write("</script>"+"\n")