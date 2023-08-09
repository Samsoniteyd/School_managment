
    $(document).ready(function(){
        $(".submitBtn").on('click', function(){
           var _checkedAns= $("input[name='answer']:checked").val();
           if(_checkedAns==undefined){
               alert('please select option!!');
               return false;
           }

        });

// timer 
	// $(".timer").countdowntimer({
	// 	seconds : 10,
    //     size : "sm",
    //     timeUp:function(){
    //         location.reload();
           
    //     }
	// });
    });


    // " {{question.time_limit}} "
    // $(".skipBtn").trigger('click');



//   swiper 
//   swiper 
let swiper = new Swiper(".mySwiper", {
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });