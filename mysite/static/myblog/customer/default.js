$(function() {

    $('[data-toggle=tooltip]').tooltip();

    $("a#writeDoc").click(function() {
        $("div#editor").fadeIn('slow');
        $("div#documents").fadeOut('slow');
    });

    $("a#loadDoc").click(function() {
        $("div#editor").fadeOut('slow');
        $("div#documents").fadeIn('slow');
    });

    $("nav li").click(function() {
        $("nav li").removeClass("active");
        $(this).addClass("active");
    });

    // ****************check username*********************
    $("#register-form #login-mail").change(function() {
        var action = $("#register-form").attr("action");
        var uname = $(this).val();
        $.ajax({
            url: action,
            data: {
                "username": uname
            },
            type: 'post',
            cache: false,
            success: function(result) {
                if (result.result == 1) {
                    msgbox("用户名已经被使用，请尝试其它的用户名！", "danger");
                } else {
                    $("#msgbox").fadeOut('slow');
                }
            },
        });
    });
    // *********************register*************************
    $("#register-form #register").click(function() {
        var action = $("#register-form").attr("action");
        var fname = $("#register-form #first-name").val();
        var lname = $("#register-form #last-name").val();
        var uname = $("#register-form #login-mail").val();
        var upass = $("#register-form #login-pass").val();
        var cpass = $("#register-form #pass-confirm").val();
        var link = $("#register-form #goLogin").attr("href");

        if (upass != cpass) {
            msgbox("输入的密码不一致");
        }

        $.ajax({
            url: action,
            data: {
                "username": uname,
                'lastname': lname,
                'firstname': fname,
                'password': upass
            },
            type: 'post',
            cache: false,
            success: function(result) {
                if (result.result == 1) {
                    msgbox("用户名已经被使用，请尝试其它的用户名！", "danger");
                } else if (result.result == 2) {
                    msgbox("用户名不是一个邮箱账号，或者密码强度不够，请检查！", "danger");
                } else if (result.result == 3) {
                    msgbox("姓名不能为空！");
                } else if (result.result == 0) {
                    msgbox("恭喜注册成功，请<a href='" + link + "'>登录>></a>", "success");
                }
            },
        });

    });
    // ********************login*****************
    $("#userauth-form #login").click(function() {
        var action = $("#userauth-form").attr("action");
        var uname = $("#userauth-form #login-mail").val();
        var upass = $("#userauth-form #login-pass").val();
        var link = $("#userauth-form #goRegister").attr("href");

        $.ajax({
            url: action,
            data: {
                "username": uname,
                'password': upass
            },
            type: 'post',
            cache: false,
            success: function(result) {
                if (result.loginCode == 0) {
                    window.location = result.redirection;
                } else {
                    msgbox("用户名或密码错误，还没有账号？请  <a href='" + link + "'>注册>></a>", "info");
                }
            },
        });
    });


    /************** modify boke *************/
    $("#modify-form * #delete").bind("click", function() {
        var obj = $(this).parent().parent();
        var link = obj.attr("action");
        var value = obj.attr("bokeid");

        $("#confirm").modal('show');
        $("#confirm #yes").click(function() {
            $.ajax({
                url: link,
                data: {
                    "blogid": value
                },
                type: 'post',
                cache: false,
                success: function(result) {
                    $("#confirm").modal('hide');
                    if (result.delCode == 0) {
                        obj.parent().parent().parent().parent().hide();
                        msgbox("数据已删除！", "success")
                    } else {
                        msgbox("删除失败，请刷新页面再次尝试！", "danger")
                    }
                },
            });
        });

    });

    //msg box function
    function msgbox() {
        var msg = arguments[0] ? arguments[0] : "Message lost.";
        var level = arguments[1] ? arguments[1] : "info";
        var time_show_range = arguments[2] ? arguments[2] : 5000;
        var messagebox = $("#msgbox");

        if (level == "info") {
            messagebox.addClass("msgbox msgbox-info");
            messagebox.html("<span class=\"fui-info-circle\"></span> " + msg);
        } else if (level == "success") {
            messagebox.addClass("msgbox msgbox-success");
            messagebox.html("<span class=\"fui-check-circle\"></span> " + msg);
        } else if (level == "waring") {
            messagebox.addClass("msgbox msgbox-waring");
            messagebox.html("<span class=\"fui-alert-circle\"></span> " + msg);
        } else {
            messagebox.addClass("msgbox msgbox-danger");
            messagebox.html("<span class=\"fui-cross-circle\"></span> " + msg);
        }

        messagebox.fadeIn('slow');
        setTimeout(function() {
            messagebox.fadeOut('slow');
        }, time_show_range);
    }

});
