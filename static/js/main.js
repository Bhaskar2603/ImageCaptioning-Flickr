function toggleWeatherPrediction() {
  var weatherDiv = document.getElementById("weatherPrediction");
  if (weatherDiv.style.display === "none" || weatherDiv.style.display === "") {
    weatherDiv.style.display = "block";
  } else {
    weatherDiv.style.display = "none";
  }
}

$(document).ready(function(){
        $('#imageUpload').change(function(){
            const file = $(this)[0].files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                   $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                    $('.image-section').show();
                }
                reader.readAsDataURL(file);
            }
        });
        $('form').on('submit', function(event){
            event.preventDefault();
            var formData = new FormData($('form')[0]);
            $.ajax({
                type: 'POST',
                url: '/predict',
                data: formData,
                contentType: false,
                cache: false,
                processData: false,
                success: function(response){
                    $('#result').text(response.caption);
                }
            });
        });

    });