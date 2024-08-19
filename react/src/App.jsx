import React, { useRef, useState } from "react";
import "./App.css";

// Import the season detail components
import SpringDetails from "../components/spring";
import FallDetails from "../components/fall";
import SummerDetails from "../components/summer";
import WinterDetails from "../components/winter";

function App() {
  const [file, setFile] = useState(null);
  const [showModal, setShowModal] = useState(false); // State to manage the modal visibility for no face detected
  const [showSeasonModal, setShowSeasonModal] = useState(false); // State to manage the season details modal
  const [season, setSeason] = useState("");
  const fileInputRef = useRef(null);

  const handleSpanClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      document.getElementById("label").classList.add("hidden");
      document
        .getElementById("startButton")
        .classList.remove("invisible");
      document.getElementById("image").classList.remove("hidden");
      document.getElementById("image").src =
        URL.createObjectURL(selectedFile);
    }
  };

  const analyzeImage = () => {
    const formData = new FormData();
    formData.append("file", file);

    circle.classList.add("fast");
    startButton.classList.add("invisible");

    fetch("http://127.0.0.1:5000/analyze", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        console.log(data.result);
        if (
          ["winter", "fall", "summer", "spring"].includes(data.result)
        ) {
          circle.classList.add(data.result);
          setSeason(data.result);
          startButton.classList.add("hidden");
          detailButton.classList.remove("hidden");
        } else {
          startButton.classList.remove("invisible");
          setShowModal(true); // Show modal if result is unexpected
        }
        circle.classList.remove("fast");
      })
      .catch((err) => console.error("Error", err));
  };

  const closeModal = () => {
    setShowModal(false); // Hide the modal
  };

  const closeSeasonModal = () => {
    setShowSeasonModal(false); // Hide the season details modal
  };

  const renderSeasonDetails = () => {
    switch (season) {
      case "spring":
        return <SpringDetails />;
      case "summer":
        return <SummerDetails />;
      case "fall":
        return <FallDetails />;
      case "winter":
        return <WinterDetails />;
      default:
        return null;
    }
  };

  return (
    <>
      <div className="app-container">
        <header className="app-header">
          <div className="logo">ColorUs</div>
          <div className="justify-center items-center text-center text-5xl mb-10">
            {season.slice(0, 1).toUpperCase() +
              season.slice(1).toLowerCase()}
          </div>
        </header>
        <main className="main-content">
          <div className="image-placeholder" id="circle">
            <span
              id="label"
              className="flex items-center justify-center w-full h-full rounded-xl p-2"
              onClick={() => fileInputRef.current.click()}>
              Upload an image
            </span>
            <input
              type="file"
              id="fileInput"
              name="img"
              accept="image/*"
              ref={fileInputRef}
              className="hidden"
              onChange={handleFileChange}
            />
            <img
              id="image"
              className="hidden w-full h-full rounded-full"
              alt="Uploaded"
              onClick={handleSpanClick}
            />
          </div>
        </main>
        <button
          id="startButton"
          className="invisible m-8 bg-transparent text-blue-700 font-semibold py-2 px-4 border border-blue-500 rounded text-2xl"
          onClick={analyzeImage}>
          Start!
        </button>
        <button
          id="detailButton"
          className="hidden m-8 bg-transparent text-blue-700 font-semibold py-2 px-4 border border-blue-500 rounded text-2xl"
          onClick={() => setShowSeasonModal(true)}>
          Details
        </button>
      </div>

      {/* No face detected modal */}
      {showModal && (
        <div
          id="popup_modal"
          tabIndex="-1"
          className="fixed inset-0 z-50 flex justify-center items-center bg-black bg-opacity-50">
          <div className="relative p-4 w-full max-w-md max-h-full">
            <div className="relative bg-white rounded-lg shadow dark:bg-gray-700">
              <button
                type="button"
                className="absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                onClick={closeModal} // Attach the close modal event handler
              >
                <svg
                  className="w-3 h-3"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 14 14">
                  <path
                    stroke="currentColor"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
                  />
                </svg>
                <span className="sr-only">Close modal</span>
              </button>
              <div className="p-4 md:p-5 text-center">
                <svg
                  className="mx-auto mb-4 text-gray-400 w-12 h-12 dark:text-gray-200"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 20 20">
                  <path
                    stroke="currentColor"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M10 11V6m0 8h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
                  />
                </svg>
                <h3 className="mb-1 text-lg font-normal text-gray-500 dark:text-gray-400">
                  No face detected.
                </h3>
                <h3 className="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">
                  Please upload another image.
                </h3>
                <button
                  onClick={closeModal} // Attach the close modal event handler
                  type="button"
                  className="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">
                  Close
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Season details modal */}
      {showSeasonModal && (
        <div
          id="season_modal"
          tabIndex="-1"
          className="fixed inset-0 z-50 flex justify-center items-center bg-black bg-opacity-50">
          <div className="relative p-4 w-full max-w-md max-h-full">
            <div className="relative bg-white rounded-lg shadow dark:bg-gray-700">
              <button
                type="button"
                className="absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                onClick={closeSeasonModal} // Attach the close season modal event handler
              >
                <svg
                  className="w-3 h-3"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 14 14">
                  <path
                    stroke="currentColor"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
                  />
                </svg>
                <span className="sr-only">Close modal</span>
              </button>
              <div className="p-4 md:p-5">
                {renderSeasonDetails()}
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

export default App;