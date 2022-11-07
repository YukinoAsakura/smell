console.log("str");
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
  console.log("str");
  var max=0;
  var al=document.getElementById("alert_text");
  if (max <=100){
    al.textContent=String("安全です")
  }
  console.log("fin");
};