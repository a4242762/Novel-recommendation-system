$(function () {
    // 获取主页面传递过来的数据
    // console.log('进入这里')
    var href = window.location.search;
    var arr = href.split('=');
    var words = arr[1];

    // console.log(words)
    $.ajax({
        url: 'http://localhost:8000/App/return_data/',
        type: 'get',
        dataType: 'jsonp',
        async:true,
        content_type: '',
        data: {
            word: words,
            page: '1'
        },
    })
        .done(function (data) {
            console.log(data)
        })
});
