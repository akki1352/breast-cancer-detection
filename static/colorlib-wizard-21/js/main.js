$(function(){
    $("#form-register").validate({
        rules: {
            password : {
                required : true,
            },
            confirm_password: {
                equalTo: "#password"
            }
        },
        messages: {
            username: {
                required: "Please provide an username"
            },
            email: {
                required: "Please provide an email"
            },
            password: {
                required: "Please provide a password"
            },
            confirm_password: {
                required: "Please provide a password",
                equalTo: "Please enter the same password"
            }
        }
    });
    $("#form-total").steps({
        headerTag: "h2",
        bodyTag: "section",
        transitionEffect: "fade",
        // enableAllSteps: true,
        autoFocus: true,
        transitionEffectSpeed: 500,
        titleTemplate : '<div class="title">#title#</div>',
        labels: {
            previous : 'Back',
            next : '<i class="zmdi zmdi-arrow-right"></i>',
            finish : 'Predict Cancer',
            current : ''
        },
        onStepChanging: function (event, currentIndex, newIndex) { 
            console.log(event);
            var radius_mean = $('#radius_mean').val();
            var texture_mean = $('#texture_mean').val();
            var texture_mean = $('#texture_mean').val();
            var texture_mean = $('#texture_mean').val();
            var texture_mean = $('#texture_mean').val();
            var compactness_mean = $('#compactness_mean').val();
            var concavity_mean = $('#concavity_mean').val();
            var concave_points_mean = $('#concave_points_mean').val();
            var symmetry_mean = $('#symmetry_mean').val();
            var fractal_dimension_mean = $('#fractal_dimension_mean').val();
            var radius_se = $('#radius_se').val();
            var texture_se = $('#texture_se').val();
            var texture_se = $('#texture_se').val();
            var texture_se = $('#texture_se').val();
            var texture_se = $('#texture_se').val();
            var compactness_se = $('#compactness_se').val();
            var concavity_se = $('#concavity_se').val();
            var concave_points_se = $('#concave_points_se').val();
            var symmetry_se = $('#symmetry_se').val();
            var fractal_dimension_se = $('#fractal_dimension_se').val();
            var radius_worst = $('#radius_worst').val();
            var texture_worst = $('#texture_worst').val();
            var texture_worst = $('#texture_worst').val();
            var texture_worst = $('#texture_worst').val();
            var texture_worst = $('#texture_worst').val();
            var compactness_worst = $('#compactness_worst').val();
            var concavity_worst = $('#concavity_worst').val();
            var concave_points_worst = $('#concave_points_worst').val();
            var symmetry_worst = $('#symmetry_worst').val();
            var fractal_dimension_worst = $('#fractal_dimension_worst').val();
            // var email = $('#email').val();
            // var cardtype = $('#card-type').val();
            // var cardnumber = $('#card-number').val();
            // var cvc = $('#cvc').val();
            // var month = $('#month').val();
            // var year = $('#year').val();

            // $('#username-val').text(username);
            // $('#email-val').text(email);
            // $('#card-type-val').text(cardtype);
            // $('#card-number-val').text(cardnumber);
            // $('#cvc-val').text(cvc);
            // $('#month-val').text(month);
            // $('#year-val').text(year);

            $("#form-register").validate().settings.ignore = ":disabled,:hidden";
            return $("#form-register").valid();
        },
        onFinished: function (event, currentIndex) {
            console.log(event);
            $("#form-register").submit();
            $('#loading').css('visibility', 'visible');
        }
    });

    
});
