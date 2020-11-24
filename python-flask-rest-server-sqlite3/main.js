//https://developer.mozilla.org/ja/docs/Web/API/Fetch_API/Using_Fetch

fetch("http://0.0.0.0:3000/MyBookmark/get/1", {
  method: "GET",
  mode: "cors",
})
  .then((res) => {
    return res.json();
  })
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error("Error:", error);
  });

fetch("http://0.0.0.0:3000/MyBookmark/get/7526886281", {
  method: "GET",
  mode: "cors",
})
  .then((res) => {
    return res.json();
  })
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error("Error:", error);
  });

fetch("http://0.0.0.0:3000/MyBookmark/delete/7526886281", {
  method: "DELETE",
  mode: "cors",
})
  .then((data) => {
    console.log("Success:", data);
  })
  .catch((error) => {
    console.error("Error:", error);
  });

let targetItem = { url: "http://localhost", title: "うんこ" };

fetch("http://0.0.0.0:3000/MyBookmark/create", {
  method: "POST",
  mode: "cors",
  body: JSON.stringify(targetItem),
})
  .then((res) => {
    return res.json();
  })
  .then((data) => {
    console.log("Success:", data);
  })
  .catch((error) => {
    console.error("Error:", error);
  });

let targetItem = { url: "http://morimori.com", title: "もりもり" };

fetch("http://0.0.0.0:3000/MyBookmark/update/7526886281", {
  method: "PATCH",
  mode: "cors",
  body: JSON.stringify(targetItem),
})
  .then((res) => {
    return res.json();
  })
  .then((data) => {
    console.log("Success:", data);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
