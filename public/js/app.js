$("#submit").click( function () {
    var ihsg = $('#ihsg').val();
    var unit = $('#unit').val();
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
    $.ajax({
    url: '/ml/predictnab',
    method: 'POST',
    data: {
      'ihsg': ihsg,
      'unit': unit,
    },
    dataType: 'json',
    success: function (data) {
        // alert('Result : ' + data.result);
        // console.log(data);
        // console.log(data.result);
        $('#result').text('Prediksi NAB : ' + data.result)
    }
  });
});