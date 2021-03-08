//==================================
//副程式 : 新增textarea(Test Case、Mutant)
//==================================
function Add_CT() {
    //暫存新的Editor
    let newmyCodeMirror;
    //新增TEXTAREA
    let btn = document.createElement("TEXTAREA");
    //預設內容
    let btn_text = document.createTextNode("#CT...");
    // 現在CT數量
    let check_count = calculation();

    //設定外部id
    btn.setAttribute("id", "CT_" + (check_count + 1));
    //設定外部name
    btn.setAttribute("name", "mutant" + (check_count + 1));
    //放入預設內容
    btn.appendChild(btn_text);

    //新增到畫面上
    document.getElementById("Area_of_CT").appendChild(btn);

    //建立Editor
    newmyCodeMirror = CodeMirror.fromTextArea(document.getElementById("CT_" + (check_count + 1)), {
        mode: "python",
        lineNumbers: true,
        foldGutter: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
        readOnly: true
    });
    //大小(W,H)
    newmyCodeMirror.setSize(400, 200);
}

//==================================
//副程式 : 新增textarea(Editor)
//==================================
function Add_Editor(codemirror_array,count){
    //暫存新的Editor
        let newmyCodeMirror;
        //新增TEXTAREA
        let btn = document.createElement("TEXTAREA");
        //預設內容
        let btn_text = document.createTextNode("#Coding...");

        //設定外部id
        btn.setAttribute("id", "code-python" + "-" + (count + 1));
        //設定外部name
        btn.setAttribute("name", "code" + (count + 1));
        //放入預設內容
        btn.appendChild(btn_text);

        //新增到畫面上
        document.getElementById("Area_of_Editor").appendChild(btn);

        //建立Editor
        newmyCodeMirror = CodeMirror.fromTextArea(document.getElementById("code-python" + "-" + (count + 1)), {
            mode: "python",
            lineNumbers: true,
            foldGutter: true,
            gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"]
        });
        //大小(W,H)
        //newmyCodeMirror.setSize(500, 300)
        //放入codemirror_array
        codemirror_array.push(newmyCodeMirror);
        //textarea總數量 + 1
        count = count + 1

}

//==================================
//副程式 : 計算CT數量
//==================================
function calculation() {
    let check_count = 0;
    while (document.getElementById("CT_" + String(check_count + 1))) {
        check_count = check_count + 1;
        console.log("check_count", check_count);
    }
    return check_count
}


//==================================
//副程式 : Initial Editor
//==================================
function Initial_Editor(te_python,codemirror_array){
    let myCodeMirror
    myCodeMirror = CodeMirror.fromTextArea(te_python, {
        mode: "python",
        lineNumbers: true,
        foldGutter: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"]
    });
    //大小(W,H)
    myCodeMirror.setSize(900, 800)
    //放入codemirror_array
    codemirror_array.push(myCodeMirror);

}

//==================================
//副程式 : Initial Area_of_CT
//==================================
function Initial_CT(CT_count){
    for (let i = 1; i <= CT_count; i++) {
        let CT_id = "CT_" + String(i);
        let temp_CT = document.getElementById(String(CT_id));
        let temp_codemirror

        temp_codemirror = CodeMirror.fromTextArea(temp_CT, {
            mode: "python",
            lineNumbers: true,
            foldGutter: true,
            gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
            //唯獨模式
            readOnly: true
        });
        //大小(W,H)
        temp_codemirror.setSize(400, 150)
    }
}

