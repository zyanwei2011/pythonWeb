$(function(){
  $('#login').click(function(){
    // 获取账号密码
    var user = $('#username').val();
    var pwd = $('#password').val();

    // 方式二
    $.ajax({
        url: '/api/login',
        type: 'post',
        data: {'user': user, 'pwd': pwd},
        dataType: 'json'
    }).done(function(data){
        if (data.code === 1){
            alert(data.msg);
        }else{
            alert(data.msg);
        }
    }).fail(function(){
        alert('请求失败')
    })
});


  var pro = $('#pro')
  $.ajax({
    url: '/api/pro_list',    
    type: 'get',
    data: '',
    dataType: 'json',
  }).done(function(data){
    if (data.code === 1){
      var res = data.data
      for (item in res){
        var option = '<option value=' + res[item].id + '>' + res[item].title + '</option>'
        pro.append(option);
      }
    }else{
      alert('请求失败')
    };
  });

  // 二级下拉框
  pro.change(function(){
    var pro_id = pro.val();
    $.ajax({
      url: '/api/interface',    
      type: 'post',
      data: {'pro_id': pro_id},
      dataType: 'json',
    }).done(function(data){
      var inter = $('#interface');
      if (data.code === 1){
        inter.empty();  // 清空二级下拉框上一次选择内容
        var res = data.data
        for (item in res){
          var option = '<option value=>' + res[item].name + '</option>'
          inter.append(option);
        }
      }else{
        alert('请求失败')
      };
    });
  })

});
