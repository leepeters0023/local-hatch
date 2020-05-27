/*async function getCodes() {
  for (let i = 0; i < 999; i++) {
   fetch(`https://www.orvis.com/fishing_report.aspx?locationid=${i}`)
      .then(response => {
        if (response.ok) {
          console.log('ok')
        } else {
          console.log(response.statusCode)
        }
      })
      .catch(error => console.log('error is', error));
  }
}
*/
getCodes() 
function getCodes() {
  for (let i = 0; i < 999; i++) {
fetch(`https://www.orvis.com/fishing_report.aspx?locationid=${i}`)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.blob();
  })
  .then(myBlob => {
    myImage.src = URL.createObjectURL(myBlob);
  })
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
  });
}}