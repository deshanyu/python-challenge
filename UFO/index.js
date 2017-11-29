// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $datetimeInput = document.querySelector("#datetime");
var $stateInput = document.querySelector("#state");
var $searchBtn = document.querySelector("#search");
var $loadMoreBtn = document.querySelector("#load-btn");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Set filteredAddresses to addressData initially
var filteredAddresses = dataSet;
// Set a startingIndex and resultsPerPage variable
var startingIndex = 0;
var resultsPerPage = 50;

// renderTable renders the filteredAddresses to the tbody
function renderTable() {
  // $tbody.innerHTML = "";
  // Set the value of endingIndex to startingIndex + resultsPerPage
  var endingIndex = startingIndex + resultsPerPage;
  // Get a section of the addressData array to render
   // alert("startingIndex:"+ startingIndex);
  alert("startingIndex:"+ startingIndex + "endingIndex:"+ endingIndex);
  var addressSubset = dataSet.slice(startingIndex, endingIndex);
  for (var i = 0; i < addressSubset.length; i++) {
    // Get the current address object and its fields
    var address = addressSubset[i];
    var fields = Object.keys(address);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i + startingIndex);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the address object, create a new cell and set its inner text to be the current value at the current address's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = address[field];
    }
  }
}

function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterDatetime = $datetimeInput.value.trim().toLowerCase();
  var filterState = $stateInput.value.trim().toLowerCase();

  // Set filteredAddresses to an array of all addresses whose "state" matches the filter
  filteredAddresses = dataSet.filter(function(address) {
    var addressDatetime = address.datetime.toLowerCase();
    var addressState = address.state.toLowerCase();
   // if (error) {return error};
    // If true, add the address to the filteredAddresses, otherwise don't add it to filteredAddresses
    return (addressState === filterState && addressDatetime === filterDatetime); 
  });
  renderTable();
}

// Add an event listener to the button, call handleButtonClick when clicked
$loadMoreBtn.addEventListener("click", handleButtonClick);

function handleButtonClick() {
  // Increase startingIndex by resultsPerPage, render the next section of the table
  startingIndex += resultsPerPage;
  renderTable();
  
  // Check to see if there are any more results to render
  if (startingIndex + resultsPerPage >= dataSet.length) {
    $loadMoreBtn.classList.add("disabled");
    $loadMoreBtn.innerText = "All Addresses Loaded";
    $loadMoreBtn.removeEventListener("click", handleButtonClick);
  }
}



// Render the table for the first time on page load
renderTable();


