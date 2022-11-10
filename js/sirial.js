var time=0;
async function sirial(){
  const filter = {
    usbVendorId: 0x2341 // Arduino SA
  };

  try {
    const port= await navigator.serial.requestPort({filters: [filter]});
    // Continue connecting to |port|.
    console.log("hello")
  } catch (e) {
    // Permission to access a device was denied implicitly or explicitly by the user.
  }
  console.log(filter.value)
  await port.open({ baudRate:115200});

  const encoder = new TextEncoder();
  const writer = port.writable.getWriter();
  writer.write(encoder.encode("AT"));

  const decoder = new TextDecoder();
  const reader = port.readable.getReader();
  const { value, done } =async () => { await reader.read();}
  console.log(decoder.decode(value));
  // Expected output: OK

};

function alertTex(){
  var max=0; 

  setInterval(timefunc,1000);
  document.getElementById('target').classList.toggle('gradation');
  
};

function timefunc(){
  time = time +1;
  console.log(time);
  if (time == 21){
    document.getElementById('btn_audio1').currentTime = 0; //連続クリックに対応
    document.getElementById('btn_audio1').play(); //クリックしたら音を再生
  }
  else if(time == 41){
    document.getElementById('btn_audio2').currentTime = 0; //連続クリックに対応
    document.getElementById('btn_audio2').play(); //クリックしたら音を再生
  }

  var al=document.getElementById("alert_text");
  if (time <=10){
    al.textContent=String("安全です")
  }
  else if(21 == time){
    al.textContent=String("通知に気を付けて作業してください")
  }
  else if(41 == time){
    al.textContent=String("今すぐ退避してください")
  }
};

function stop(){
  var an = document.getElementById('target');
  if(an.style.animationPlayState == "running"){
     an.style.animationPlayState = "paused";
  }else{
     an.style.animationPlayState = "running";
  }
  
}
