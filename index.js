// Assuming you have a JSON file named data.json in the same directory

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const luckyButton = document.getElementById('luckyButton');
    const randomLocationButton = document.getElementById('randomLocation');
    const pickLocationButton = document.getElementById('pickLocation');
    const locationOptions = document.getElementById('locationOptions');
    const showFoodDiv = document.getElementById('showFood');
    const passButton = document.getElementById('pass');
    const smashButton = document.getElementById('smash');
    let currentStoreIndex = null;
    let storesData = [];
    const searchResults = document.getElementById('searchResults');
    let currentMode = ''; // 'random' for random location mode, 'pick' for pick location mode

    // Function to display search results
    const displaySearchResults = (stores) => {
        searchResults.innerHTML = '';
        if (stores.length > 0) {
            stores.slice(0, 5).forEach(store => {
                const resultItem = document.createElement('a');
                resultItem.href = '#';
                resultItem.classList.add('list-group-item', 'list-group-item-action');
                resultItem.innerHTML = `
                    <div>
                        ${store.storeName} ${store.vegetarian ? `<img src="veg.png" alt="Vegetarian" style="height: 20px;"/>` : ''}
                        <br>
                        ${store.location} <br>
                        ${store.openingHours}
                        
                    </div>`;
                resultItem.addEventListener('click', () => {
                    // Perform action when a search result is clicked
                });
                searchResults.appendChild(resultItem);
            });
            searchResults.style.display = 'block';
        } else {
            searchResults.style.display = 'none';
        }
    };
    
    // Event listener for search input
    searchInput.addEventListener('input', () => {
        const searchText = searchInput.value.toLowerCase();
        if (searchText.trim() === '') {
            displaySearchResults([]);
        } else {
            const filteredStores = storesData.filter(store => 
                store.storeName.toLowerCase().includes(searchText) || 
                store.location.toLowerCase().includes(searchText)
            );
            displaySearchResults(filteredStores);
        }
    });

    // Fetch stores data from the JSON file
    storesData = [
        {
            "storeName": "Mixed veg rice",
            "location": "Canteen 2",
            "vegetarian": true,
            "openingHours": "10 am\u20139:30 pm"
        },
        {
            "storeName": "Taiwan cuisine",
            "location": "Canteen 2",
            "vegetarian": false,
            "openingHours": "11 am\u20139:30 pm"
        },
        {
            "storeName": "Mini wok",
            "location": "Canteen 2",
            "vegetarian": false,
            "openingHours": "12 am\u20139:30 pm"
        },
        {
            "storeName": "Korean cuisine",
            "location": "Canteen 2",
            "vegetarian": false,
            "openingHours": "13 am\u20139:30 pm"
        },
        {
            "storeName": "Xiao Long Bao",
            "location": "Canteen 2",
            "vegetarian": false,
            "openingHours": "14 am\u20139:30 pm"
        },
        {
            "storeName": "Chicken rice",
            "location": "Canteen 2",
            "vegetarian": false,
            "openingHours": "15 am\u20139:30 pm"
        },
        {
            "storeName": "Ramen",
            "location": "Canteen 2",
            "vegetarian": false,
            "openingHours": "16 am\u20139:30 pm"
        },
        {
            "storeName": "Thai cuisine",
            "location": "Canteen 2",
            "vegetarian": false,
            "openingHours": "17 am\u20139:30 pm"
        },
        {
            "storeName": "Western cuisine",
            "location": "Canteen 2",
            "vegetarian": false,
            "openingHours": "18 am\u20139:30 pm"
        },
        {
            "storeName": "Mcdonalds",
            "location": "North Spine",
            "vegetarian": true,
            "openingHours": "7 am\u201310 pm"
        },
        {
            "storeName": "popeyes",
            "location": "North Spine",
            "vegetarian": false,
            "openingHours": ""
        },
        {
            "storeName": "Encik Tan",
            "location": "North Spine",
            "vegetarian": true,
            "openingHours": ""
        },
        {
            "storeName": "Blue ocean",
            "location": "North Spine",
            "vegetarian": true,
            "openingHours": ""
        },
        {
            "storeName": "Starbucks",
            "location": "North Spine",
            "vegetarian": true,
            "openingHours": "7 am\u201310 pm"
        },
        {
            "storeName": "Subway",
            "location": "North Spine",
            "vegetarian": true,
            "openingHours": "7am to 8pm"
        },
        {
            "storeName": "Pasta express",
            "location": "North Spine",
            "vegetarian": true,
            "openingHours": "10.30am to 7.30pm"
        },
        {
            "storeName": "Mr bean",
            "location": "North Spine",
            "vegetarian": true,
            "openingHours": ""
        },
        {
            "storeName": "Dim Sum",
            "location": "South Spine",
            "vegetarian": false,
            "openingHours": "7am to 8pm"
        },
        {
            "storeName": "Japanese & Korean",
            "location": "South Spine",
            "vegetarian": false,
            "openingHours": "7am to 8pm"
        },
        {
            "storeName": "Bimbowl Jjajang",
            "location": "South Spine",
            "vegetarian": false,
            "openingHours": "7am to 8pm"
        },
        {
            "storeName": "Hot pot snail",
            "location": "South Spine",
            "vegetarian": true,
            "openingHours": "7am to 8pm"
        },
        {
            "storeName": "Yong Tou foo",
            "location": "South Spine",
            "vegetarian": true,
            "openingHours": "7am to 8pm"
        },
        {
            "storeName": "Braised Duck Rice",
            "location": "South Spine",
            "vegetarian": false,
            "openingHours": "7am to 8pm"
        },
        {
            "storeName": "Mixed Veg rice",
            "location": "South Spine",
            "vegetarian": true,
            "openingHours": "7am to 8pm"
        },
        {
            "storeName": "Paik's Bibim",
            "location": "North Spine",
            "vegetarian": true,
            "openingHours": "10am to 9pm"
        }
    ]
    
    

    luckyButton.addEventListener('click', () => {
        searchResults.style.display = 'none'; // Hide search results
        document.getElementById('luckyOptions').style.display = 'block'; // Show lucky options
        showFoodDiv.style.display = 'none'; // Hide food options
    });

    randomLocationButton.addEventListener('click', () => {
        currentMode = 'random'; // Set mode to random
        document.getElementById('luckyOptions').style.display = 'none'; // Hide lucky options
        showRandomStore(); // Show a random store
    });

    pickLocationButton.addEventListener('click', () => {
        currentMode = 'pick'; // Set mode to pick
        document.getElementById('luckyOptions').style.display = 'none'; // Hide lucky options
        searchResults.style.display = 'none'; // Hide search results
        showLocationOptions(); // Show location options
    });

    const showLocationOptions = () => {
        locationOptions.innerHTML = ''; // Clear previous options
        const uniqueLocations = [...new Set(storesData.map(store => store.location))]; // Get unique locations
        uniqueLocations.forEach(location => {
            const button = document.createElement('button');
            button.textContent = location;
            button.className = 'btn btn-secondary mb-2';
            button.onclick = () => displayRandomStoreAtLocation(location);
            locationOptions.appendChild(button);
        });
        locationOptions.style.display = 'block';
    };

    const showRandomStore = () => {
        const randomIndex = Math.floor(Math.random() * storesData.length);
        displayStoreDetails(randomIndex);
    };
    const displayStoreDetails = (index, stores = storesData) => {
        const store = stores[index];
        if (store) {
            showFoodDiv.innerHTML = `
                <div>
                    <h3>${store.storeName}</h3>
                    <p>${store.location}</p>
                    <p>${store.vegetarian ? '<img src="veg.png" alt="Vegetarian" style="height: 20px;"/>':"" }</p>
                    <p>${store.openingHours}</p>
                    <button class="btn btn-danger" id="pass">Pass</button>
                    <button class="btn btn-success" id="smash">Smash</button>
                </div>
            `;
            showFoodDiv.style.display = 'block';
    
            // Event listeners for Smash and Pass buttons
            document.getElementById('smash').addEventListener('click', () => {
                console.log('Smash')
                window.location.href = 'thanks.html'; // Redirect to thanks page
            });
            document.getElementById('pass').addEventListener('click', () => {
                // console.log("currentMode",currentMode)
                if (currentMode === 'random') {
                    // console.log("random")
                    showRandomStore(); // Display a store from any location
                } else if (currentMode === 'pick') {
                    displayRandomStoreAtLocation(stores[0].location); // Display another store at the same location
                }
            });
        }
    };
    
    const displayRandomStoreAtLocation = (location) => {
        locationOptions.style.display = 'none'; // Hide location options
        const storesAtLocation = storesData.filter(store => store.location === location);
        if (storesAtLocation.length > 0) {
            const randomIndex = Math.floor(Math.random() * storesAtLocation.length);
            displayStoreDetails(randomIndex, storesAtLocation);
        }
    };

    passButton.addEventListener('click', () => {
        // console.log("currentMode",currentMode)
        if (currentMode === 'random') {
            // console.log("random")
            showRandomStore(); // Display a store from any location
        } else if (currentMode === 'pick') {
            displayRandomStoreAtLocation(stores[0].location); // Display another store at the same location
        }
    });

    smashButton.addEventListener('click', () => {
        window.location.href = 'thanks.html'; // Redirect to survey page
    });

    function displayFoodOptions(index, pass = false) {
        const store = storesData[index];
        if (store) {
            showFoodDiv.style.display = 'block';
            showFoodDiv.innerHTML = '<h3>Food Option:</h3>';
            const randomFoodIndex = Math.floor(Math.random() * store.foodOptions.length);
            showFoodDiv.innerHTML += `<p>${store.foodOptions[randomFoodIndex]}</p>`;
        }
        if (pass) {
            currentStoreIndex = (currentStoreIndex + 1) % storesData.length; // Move to next store
        }
    }

    // Search functionality (for preview)
    searchInput.addEventListener('input', () => {
        const searchText = searchInput.value.toLowerCase();
        const filteredStores = storesData.filter(store => store.storeName.toLowerCase().includes(searchText) || store.location.toLowerCase().includes(searchText));
        // You can display the filteredStores below the search bar as a preview
    });
});

 
 

 