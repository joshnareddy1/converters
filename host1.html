<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Convert Everything</title>
    <!-- Tailwind CSS CDN for easy styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <!-- PDF.js library for client-side PDF text extraction -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
    <script>
        // Set the workerSrc for PDF.js
        pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
    </script>
    <style>
        /* Custom styles for a deep, vibrant, and high-quality feel */
        body {
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            overflow-x: hidden; /* Prevent horizontal scroll */
        }
        .deep-gradient-background {
            /* A deep, rich, and more professional gradient */
            background: linear-gradient(135deg, #4A148C, #7B1FA2, #C2185B); /* Deep Purple, Medium Purple, Deep Pink */
            background-size: 400% 400%;
            animation: gradientAnimation 15s ease infinite; /* Smooth animation */
        }
        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .card-shadow {
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        }
        /* Style for hidden pages */
        .page-view.hidden {
            display: none;
        }
        /* Loading spinner animation */
        .spinner {
            border: 4px solid rgba(255, 255, 255, 0.2);
            border-left-color: #fca5a5; /* Tailwind red-400 */
            border-radius: 50%;
            width: 36px;
            height: 36px;
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /*
            *** YOUR CUSTOM CSS GOES HERE ***
            You can add your project's specific CSS rules here.
        */
        .modal {
            display: none;
            position: fixed;
            z-index: 100;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0,0,0,0.6);
            justify-content: center;
            align-items: center;
        }
        .modal-content {
            background-color: #2D3748; /* Dark background for modal */
            color: #E2E8F0; /* Light text for readability */
            margin: auto;
            padding: 20px;
            border: 1px solid #4A5568;
            width: 80%;
            max-width: 500px;
            border-radius: 10px;
            text-align: center;
        }
        .close-button {
            color: #A0AEC0;
            float: right;
            font-size: 28px;
            font-weight: bold;
        }
        .close-button:hover,
        .close-button:focus {
            color: white;
            text-decoration: none;
            cursor: pointer;
        }

        /* Button Gradient Animation */
        .animated-button {
            background-size: 200% 100%;
            transition: background-position 0.5s ease;
        }
        .animated-button:hover {
            background-position: -100% 0;
        }

    </style>
</head>
<body class="min-h-screen flex flex-col items-center justify-center p-4 deep-gradient-background">

    <div class="w-full max-w-4xl bg-gray-800 bg-opacity-70 rounded-xl p-8 md:p-12 card-shadow text-center text-white">
        <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-2 animate-pulse">
            Convert Everything
        </h1>
        <p class="text-lg md:text-xl text-gray-300 mb-8">
            Just with a click
        </p>

        <!--
            ====================================================================
            *** START_YOUR_PROJECT_HTML ***
            This section now contains the HTML for the different "pages" or views.
            ====================================================================
        -->
        <div id="main-content-area" class="w-full">
            <!-- First Page: Welcome and Options -->
            <div id="welcome-page" class="page-view bg-white bg-opacity-10 rounded-lg p-8 md:p-10 card-shadow text-white text-center border border-gray-600">
                <h3 class="text-3xl font-bold mb-6 text-white">Get Started Now!</h3>
                <div class="flex flex-col md:flex-row justify-center items-center space-y-4 md:space-y-0 md:space-x-4">
                    <button id="start-button" class="animated-button w-full md:w-auto px-8 py-4 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 bg-gradient-to-r from-blue-500 to-indigo-600 hover:from-indigo-600 hover:to-blue-500">
                        Start
                    </button>
                    <button id="login-button" class="animated-button w-full md:w-auto px-8 py-4 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 bg-gradient-to-r from-green-500 to-teal-600 hover:from-teal-600 hover:to-green-500">
                        Login
                    </button>
                    <button id="use-for-free-button" class="animated-button w-full md:w-auto px-8 py-4 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 bg-gradient-to-r from-purple-500 to-pink-600 hover:from-pink-600 hover:to-purple-500">
                        Use for Free
                    </button>
                </div>
            </div>

            <!-- Login Options Page -->
            <div id="login-options-page" class="page-view hidden bg-white bg-opacity-10 rounded-lg p-8 md:p-10 card-shadow text-white text-center border border-gray-600">
                <h3 class="text-3xl font-bold mb-6 text-white">Login Options</h3>
                <div class="flex flex-col space-y-4">
                    <button class="animated-button w-full px-8 py-4 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 flex items-center justify-center bg-gradient-to-r from-red-600 to-red-800 hover:from-red-800 hover:to-red-600">
                        <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"></path><path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"></path></svg>
                        Login with Email
                    </button>
                    <button class="animated-button w-full px-8 py-4 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 flex items-center justify-center bg-gradient-to-r from-blue-700 to-blue-900 hover:from-blue-900 hover:to-blue-700">
                        <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M20 10c0-5.523-4.477-10-10-10S0 4.477 0 10c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V10h2.54V7.71c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V10h2.773l-.443 2.89h-2.33V20C16.343 19.128 20 14.991 20 10z" clip-rule="evenodd"></path></svg>
                        Login with Facebook
                    </button>
                    <button class="animated-button w-full px-8 py-4 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 flex items-center justify-center bg-gradient-to-r from-gray-700 to-gray-900 hover:from-gray-900 hover:to-gray-700">
                        <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M19.215 9.615c0-.686-.061-1.354-.182-1.996H10v3.742h5.385a4.57 4.57 0 01-1.996 2.978v2.428h3.125c1.827-1.688 2.88-4.17 2.88-7.152z" fill="#4285F4"></path><path d="M10 20c2.724 0 5.008-.897 6.677-2.433l-3.125-2.428c-.868.58-1.97.925-3.552.925-2.73 0-5.045-1.83-5.88-4.285H1.08v2.502A9.993 9.993 0 0010 20z" fill="#34A853"></path><path d="M4.12 11.667a6.002 6.002 0 010-3.334V5.833H1.08A9.993 9.993 0 000 10c0 1.932.518 3.75 1.42 5.295l3.125-2.502z" fill="#FBBC05"></path><path d="M10 3.998c1.47 0 2.78.508 3.824 1.492L16.29 2.51C14.545.925 12.35 0 10 0A9.993 9.993 0 000 10h4.12C4.955 7.83 7.27 3.998 10 3.998z" fill="#EA4335"></path></svg>
                        Login with Google
                    </button>
                    <button id="sign-in-button" class="animated-button w-full px-8 py-4 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 flex items-center justify-center bg-gradient-to-r from-indigo-600 to-indigo-800 hover:from-indigo-800 hover:to-indigo-600">
                        <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"></path></svg>
                        Sign In
                    </button>
                </div>
                <button id="back-to-welcome-from-login-button" class="mt-8 px-6 py-3 bg-gray-500 text-white font-semibold rounded-lg shadow-md hover:bg-gray-600 transition duration-300 ease-in-out">
                    &larr; Back to Welcome
                </button>
            </div>


            <!-- Next Page: Converter Options -->
            <div id="converter-page" class="page-view hidden bg-white bg-opacity-10 rounded-lg p-8 md:p-10 card-shadow text-white text-center border border-gray-600">
                <h3 class="text-3xl font-bold mb-6 text-white">Choose Your Converter</h3>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
                    <!-- Text-to-Speech Converter Option -->
                    <div id="tts-option" class="bg-white bg-opacity-5 p-6 rounded-lg shadow-md border border-gray-600 cursor-pointer hover:shadow-lg transition duration-300 ease-in-out transform hover:-translate-y-1">
                        <h4 class="text-xl font-semibold mb-2">Text-to-Speech</h4>
                        <p class="text-gray-300">Convert written text into spoken audio.</p>
                    </div>

                    <!-- Speech-to-Text Converter Option -->
                    <div id="stt-option" class="bg-white bg-opacity-5 p-6 rounded-lg shadow-md border border-gray-600 cursor-pointer hover:shadow-lg transition duration-300 ease-in-out transform hover:-translate-y-1">
                        <h4 class="text-xl font-semibold mb-2">Speech-to-Text</h4>
                        <p class="text-gray-300">Convert spoken words into written text.</p>
                    </div>

                    <!-- PDF Text Extractor Option -->
                    <div id="pdf-extractor-option" class="bg-white bg-opacity-5 p-6 rounded-lg shadow-md border border-gray-600 cursor-pointer hover:shadow-lg transition duration-300 ease-in-out transform hover:-translate-y-1">
                        <h4 class="text-xl font-semibold mb-2">PDF Text Extractor</h4>
                        <p class="text-gray-300">Extract text from PDF documents.</p>
                    </div>

                    <!-- Audio Mixer/Player Option -->
                    <div id="audio-mixer-option" class="bg-white bg-opacity-5 p-6 rounded-lg shadow-md border border-gray-600 cursor-pointer hover:shadow-lg transition duration-300 ease-in-out transform hover:-translate-y-1">
                        <h4 class="text-xl font-semibold mb-2">Audio Player</h4>
                        <p class="text-gray-300">Play audio with/without background music.</p>
                    </div>

                    <!-- Updated: AI Text-to-Image (Prompt) Option -->
                    <div id="text-to-image-option" class="bg-white bg-opacity-5 p-6 rounded-lg shadow-md border border-gray-600 cursor-pointer hover:shadow-lg transition duration-300 ease-in-out transform hover:-translate-y-1">
                        <h4 class="text-xl font-semibold mb-2">AI Text-to-Image</h4>
                        <p class="text-gray-300">Generate an image from your text prompt.</p>
                    </div>

                    <!-- NEW: Image to Anime Style (Upload) Option -->
                    <div id="image-to-anime-option" class="bg-white bg-opacity-5 p-6 rounded-lg shadow-md border border-gray-600 cursor-pointer hover:shadow-lg transition duration-300 ease-in-out transform hover:-translate-y-1">
                        <h4 class="text-xl font-semibold mb-2">Image to Anime Style</h4>
                        <p class="text-gray-300">Upload an image and convert it to anime style.</p>
                    </div>

                    <!-- NEW: Text to Video Converter Option -->
                    <div id="text-to-video-option" class="bg-white bg-opacity-5 p-6 rounded-lg shadow-md border border-gray-600 cursor-pointer hover:shadow-lg transition duration-300 ease-in-out transform hover:-translate-y-1">
                        <h4 class="text-xl font-semibold mb-2">Text-to-Video</h4>
                        <p class="text-gray-300">Generate video from text prompts.</p>
                    </div>
                </div>
                <button id="back-to-welcome-button" class="mt-4 px-6 py-3 bg-gray-500 text-white font-semibold rounded-lg shadow-md hover:bg-gray-600 transition duration-300 ease-in-out">
                    &larr; Back to Welcome
                </button>
            </div>

            <!-- Specific Converter: Text-to-Speech -->
            <div id="tts-converter-detail-page" class="page-view hidden bg-white bg-opacity-10 rounded-lg p-8 md:p-10 card-shadow text-white text-center border border-gray-600">
                <h3 class="text-3xl font-bold mb-6 text-white">Text-to-Speech Converter</h3>
                <div class="mb-6">
                    <label for="tts-text-input" class="block text-lg font-medium text-gray-300 mb-2">Enter Text to Convert:</label>
                    <textarea id="tts-text-input" class="w-full p-3 rounded-md border border-gray-600 bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 resize-y min-h-[100px]" placeholder="Type your text here..."></textarea>
                </div>
                <div class="mb-6">
                    <label for="tts-language-select" class="block text-lg font-medium text-gray-300 mb-2">Select Language/Voice:</label>
                    <select id="tts-language-select" class="w-full p-3 rounded-md border border-gray-600 bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500">
                        <!-- Voices will be populated dynamically -->
                    </select>
                </div>
                <button id="tts-convert-button" class="animated-button w-full md:w-auto px-8 py-4 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 bg-gradient-to-r from-purple-600 to-purple-800 hover:from-purple-800 hover:to-purple-600">
                    Generate Speech
                </button>
                <div id="tts-status" class="mt-4 text-sm font-semibold text-gray-400"></div>
                <div id="tts-output-container" class="mt-6 hidden">
                    <h4 class="text-xl font-semibold mb-2">Generated Audio</h4>
                    <audio id="tts-audio-player" controls class="w-full"></audio>
                </div>
                <button id="back-to-converters-from-tts" class="mt-8 px-6 py-3 bg-gray-500 text-white font-semibold rounded-lg shadow-md hover:bg-gray-600 transition duration-300 ease-in-out">
                    &larr; Back to Converters
                </button>
            </div>

            <!-- Specific Converter: Speech-to-Text -->
            <div id="stt-converter-detail-page" class="page-view hidden bg-white bg-opacity-10 rounded-lg p-8 md:p-10 card-shadow text-white text-center border border-gray-600">
                <h3 class="text-3xl font-bold mb-6 text-white">Speech-to-Text Converter</h3>
                <div class="mb-6">
                    <p class="text-lg text-gray-300 mb-4">Click the button and start speaking. The transcription will appear below.</p>
                    <button id="stt-record-button" class="animated-button w-full md:w-auto px-8 py-4 text-white font-semibold rounded-full shadow-md transition duration-300 ease-in-out transform hover:scale-105 flex items-center justify-center mx-auto bg-gradient-to-r from-red-600 to-red-800 hover:from-red-800 hover:to-red-600">
                        <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10 8a3 3 0 100-6 3 3 0 000 6zM3.465 14.493a1.23 1.23 0 00.18.72l1.652 1.653a1.23 1.23 0 00.72.18h7.966a1.23 1.23 0 00.72-.18l1.652-1.653a1.23 1.23 0 00.18-.72V11a1 1 0 112 0v3.493a3.23 3.23 0 01-.48 1.76l-1.652 1.654a3.23 3.23 0 01-1.76.48H5.465a3.23 3.23 0 01-1.76-.48l-1.652-1.654a3.23 3.23 0 01-.48-1.76V11a1 1 0 112 0v3.493z"></path></svg>
                        Start Recording
                    </button>
                    <div id="stt-status" class="mt-4 text-sm font-semibold text-gray-400"></div>
                </div>
                <div class="bg-gray-700 p-6 rounded-xl border border-gray-600 mt-6">
                    <h4 class="text-xl font-semibold mb-2">Transcribed Text</h4>
                    <div id="stt-output" class="p-4 rounded-lg bg-gray-800 min-h-[150px] border border-gray-600 overflow-y-auto text-left">
                        <p id="stt-placeholder" class="text-gray-400 italic">Transcribed text will appear here...</p>
                    </div>
                </div>
                <button id="back-to-converters-from-stt" class="mt-8 px-6 py-3 bg-gray-500 text-white font-semibold rounded-lg shadow-md hover:bg-gray-600 transition duration-300 ease-in-out">
                    &larr; Back to Converters
                </button>
            </div>

            <!-- Specific Converter: PDF Text Extractor -->
            <div id="pdf-extractor-detail-page" class="page-view hidden bg-white bg-opacity-10 rounded-lg p-8 md:p-10 card-shadow text-white text-center border border-gray-600">
                <h3 class="text-3xl font-bold mb-6 text-white">PDF Text Extractor</h3>
                <div class="mb-6">
                    <p class="text-lg text-gray-300 mb-4">Upload a PDF file to extract its text content.</p>
                    <input type="file" id="pdfFileInput" accept=".pdf" class="w-full p-4 rounded-lg bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-colors duration-200" />
                </div>
                <button id="convert-pdf-button" class="animated-button w-full md:w-auto px-8 py-4 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 bg-gradient-to-r from-green-600 to-green-800 hover:from-green-800 hover:to-green-600">
                    Extract Text
                </button>
                <div id="pdf-status" class="mt-4 text-sm font-semibold text-gray-400"></div>
                <div class="bg-gray-700 p-6 rounded-xl border border-gray-600 mt-6">
                    <h4 class="text-xl font-semibold mb-2">Extracted Text</h4>
                    <div id="pdf-output" class="p-4 rounded-lg bg-gray-800 min-h-[150px] border border-gray-600 overflow-y-auto text-left text-gray-300">
                        <p id="pdf-placeholder" class="text-gray-400 italic">Extracted text will appear here...</p>
                    </div>
                </div>
                <button id="back-to-converters-from-pdf" class="mt-8 px-6 py-3 bg-gray-500 text-white font-semibold rounded-lg shadow-md hover:bg-gray-600 transition duration-300 ease-in-out">
                    &larr; Back to Converters
                </button>
            </div>

            <!-- Specific Converter: AI Text-to-Image -->
            <div id="text-to-image-detail-page" class="page-view hidden bg-white bg-opacity-10 rounded-lg p-8 md:p-10 card-shadow text-white text-center border border-gray-600">
                <h3 class="text-3xl font-bold mb-6 text-white">AI Text-to-Image</h3>
                <div class="mb-6">
                    <p class="text-lg text-gray-300 mb-4">Enter a text prompt and generate an image.</p>
                    <textarea id="text-to-image-prompt" class="w-full p-3 rounded-md border border-gray-600 bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-indigo-500 resize-y min-h-[100px]" placeholder="A hyper-realistic photograph of a futuristic city at sunset"></textarea>
                </div>
                <button id="generate-image-button" class="animated-button w-full md:w-auto px-8 py-4 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 bg-gradient-to-r from-indigo-600 to-indigo-800 hover:from-indigo-800 hover:to-indigo-600">
                    Generate Image
                </button>
                <div id="text-to-image-status" class="mt-4 text-sm font-semibold text-gray-400"></div>
                <div class="bg-gray-700 p-6 rounded-xl border border-gray-600 mt-6 min-h-[300px] flex items-center justify-center">
                    <img id="generated-image" class="rounded-lg max-w-full max-h-[400px] hidden" alt="Generated Image">
                    <div id="image-placeholder" class="text-gray-400 italic">Generated image will appear here...</div>
                </div>
                <button id="back-to-converters-from-image-gen" class="mt-8 px-6 py-3 bg-gray-500 text-white font-semibold rounded-lg shadow-md hover:bg-gray-600 transition duration-300 ease-in-out">
                    &larr; Back to Converters
                </button>
            </div>

            <!-- Specific Converter: Image to Anime Style -->
            <div id="image-to-anime-detail-page" class="page-view hidden bg-white bg-opacity-10 rounded-lg p-8 md:p-10 card-shadow text-white text-center border border-gray-600">
                <h3 class="text-3xl font-bold mb-6 text-white">Image to Anime Style</h3>
                <div class="mb-6">
                    <p class="text-lg text-gray-300 mb-4">Upload an image and convert it to an anime style.</p>
                    <input type="file" id="anime-image-input" accept="image/*" class="w-full p-4 rounded-lg bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-pink-500 transition-colors duration-200" />
                </div>
                <button id="convert-to-anime-button" class="animated-button w-full md:w-auto px-8 py-4 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 bg-gradient-to-r from-pink-500 to-rose-600 hover:from-rose-600 hover:to-pink-500">
                    Convert to Anime
                </button>
                <div id="anime-status" class="mt-4 text-sm font-semibold text-gray-400"></div>
                <div class="bg-gray-700 p-6 rounded-xl border border-gray-600 mt-6 min-h-[300px] flex items-center justify-center">
                    <img id="anime-output-image" class="rounded-lg max-w-full max-h-[400px] hidden" alt="Anime Style Image">
                    <div id="anime-placeholder" class="text-gray-400 italic">Anime style image will appear here...</div>
                </div>
                <button id="back-to-converters-from-anime" class="mt-8 px-6 py-3 bg-gray-500 text-white font-semibold rounded-lg shadow-md hover:bg-gray-600 transition duration-300 ease-in-out">
                    &larr; Back to Converters
                </button>
            </div>

            <!-- Specific Converter: Audio Player -->
            <div id="audio-mixer-detail-page" class="page-view hidden bg-white bg-opacity-10 rounded-lg p-8 md:p-10 card-shadow text-white text-center border border-gray-600">
                <h3 class="text-3xl font-bold mb-6 text-white">Simple Audio Player</h3>
                <div class="mb-6">
                    <p class="text-lg text-gray-300 mb-4">Upload an audio file to play it.</p>
                    <input type="file" id="audioFileInput" accept="audio/*" class="w-full p-4 rounded-lg bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-colors duration-200" />
                </div>
                <audio id="audioPlayer" controls class="w-full"></audio>
                <div id="audio-status" class="mt-4 text-sm font-semibold text-gray-400"></div>
                <button id="back-to-converters-from-audio" class="mt-8 px-6 py-3 bg-gray-500 text-white font-semibold rounded-lg shadow-md hover:bg-gray-600 transition duration-300 ease-in-out">
                    &larr; Back to Converters
                </button>
            </div>

            <!-- Specific Converter: Text-to-Video -->
            <div id="text-to-video-detail-page" class="page-view hidden bg-white bg-opacity-10 rounded-lg p-8 md:p-10 card-shadow text-white text-center border border-gray-600">
                <h3 class="text-3xl font-bold mb-6 text-white">Text-to-Video Generator</h3>
                <p class="text-lg text-red-400 font-semibold mb-4">Feature not available in this client-side application.</p>
                <p class="text-md text-gray-300">
                    Text-to-video generation is an advanced feature that requires server-side processing and a specialized AI API.
                    This client-side implementation cannot perform this task.
                </p>
                <button id="back-to-converters-from-video" class="mt-8 px-6 py-3 bg-gray-500 text-white font-semibold rounded-lg shadow-md hover:bg-gray-600 transition duration-300 ease-in-out">
                    &larr; Back to Converters
                </button>
            </div>

        </div>

    </div>

    <!-- Custom Modal for Alerts -->
    <div id="custom-modal" class="modal">
        <div class="modal-content">
            <span class="close-button">&times;</span>
            <p id="modal-message" class="text-lg text-gray-200"></p>
        </div>
    </div>


    <script>
        /*
            ====================================================================
            *** START_YOUR_PROJECT_JAVASCRIPT ***
            This section contains all the logic for the "Convert Everything" app.
            ====================================================================
        */

        // ====================================================================
        //  PAGE NAVIGATION LOGIC
        // ====================================================================
        const welcomePage = document.getElementById('welcome-page');
        const loginOptionsPage = document.getElementById('login-options-page');
        const converterPage = document.getElementById('converter-page');
        const ttsDetailPage = document.getElementById('tts-converter-detail-page');
        const sttDetailPage = document.getElementById('stt-converter-detail-page');
        const pdfExtractorPage = document.getElementById('pdf-extractor-detail-page');
        const textToImagePage = document.getElementById('text-to-image-detail-page');
        const imageToAnimePage = document.getElementById('image-to-anime-detail-page');
        const audioPlayerPage = document.getElementById('audio-mixer-detail-page');
        const textToVideoPage = document.getElementById('text-to-video-detail-page');

        const allPages = [
            welcomePage,
            loginOptionsPage,
            converterPage,
            ttsDetailPage,
            sttDetailPage,
            pdfExtractorPage,
            textToImagePage,
            imageToAnimePage,
            audioPlayerPage,
            textToVideoPage
        ];

        // Function to show a specific page and hide all others
        function showPage(pageToShow) {
            allPages.forEach(page => {
                if (page === pageToShow) {
                    page.classList.remove('hidden');
                } else {
                    page.classList.add('hidden');
                }
            });
        }

        // Event listeners for top-level navigation buttons
        document.getElementById('start-button').addEventListener('click', () => showPage(converterPage));
        document.getElementById('use-for-free-button').addEventListener('click', () => showPage(converterPage));
        document.getElementById('login-button').addEventListener('click', () => showPage(loginOptionsPage));
        document.getElementById('back-to-welcome-from-login-button').addEventListener('click', () => showPage(welcomePage));
        document.getElementById('back-to-welcome-button').addEventListener('click', () => showPage(welcomePage));

        // Event listeners for converter options
        document.getElementById('tts-option').addEventListener('click', () => showPage(ttsDetailPage));
        document.getElementById('stt-option').addEventListener('click', () => showPage(sttDetailPage));
        document.getElementById('pdf-extractor-option').addEventListener('click', () => showPage(pdfExtractorPage));
        document.getElementById('text-to-image-option').addEventListener('click', () => showPage(textToImagePage));
        document.getElementById('image-to-anime-option').addEventListener('click', () => showPage(imageToAnimePage));
        document.getElementById('audio-mixer-option').addEventListener('click', () => showPage(audioPlayerPage));
        document.getElementById('text-to-video-option').addEventListener('click', () => showPage(textToVideoPage));

        // Event listeners for "back to converters" buttons on detail pages
        document.getElementById('back-to-converters-from-tts').addEventListener('click', () => showPage(converterPage));
        document.getElementById('back-to-converters-from-stt').addEventListener('click', () => showPage(converterPage));
        document.getElementById('back-to-converters-from-pdf').addEventListener('click', () => showPage(converterPage));
        document.getElementById('back-to-converters-from-image-gen').addEventListener('click', () => showPage(converterPage));
        document.getElementById('back-to-converters-from-anime').addEventListener('click', () => showPage(converterPage));
        document.getElementById('back-to-converters-from-audio').addEventListener('click', () => showPage(converterPage));
        document.getElementById('back-to-converters-from-video').addEventListener('click', () => showPage(converterPage));

        // Custom Modal Logic for alerts
        const modal = document.getElementById('custom-modal');
        const modalMessage = document.getElementById('modal-message');
        const closeModal = document.querySelector('.close-button');

        closeModal.onclick = () => modal.style.display = 'none';
        window.onclick = (event) => {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        };

        function showModal(message) {
            modalMessage.textContent = message;
            modal.style.display = 'flex';
        }

        // Helper function for exponential backoff retry
        async function fetchWithRetry(url, options, maxRetries = 3) {
            let retryCount = 0;
            while (retryCount < maxRetries) {
                try {
                    const response = await fetch(url, options);
                    if (response.ok) {
                        return response;
                    } else if (response.status === 429) {
                        const delay = Math.pow(2, retryCount) * 1000;
                        await new Promise(resolve => setTimeout(resolve, delay));
                        retryCount++;
                    } else {
                        throw new Error(`API error: ${response.statusText}`);
                    }
                } catch (e) {
                    if (retryCount >= maxRetries - 1) {
                        throw e;
                    }
                    retryCount++;
                }
            }
            throw new Error("Failed to get a successful response after multiple retries.");
        }


        // ====================================================================
        // TEXT-TO-SPEECH (TTS) LOGIC
        // ====================================================================
        const ttsTextInput = document.getElementById('tts-text-input');
        const ttsLanguageSelect = document.getElementById('tts-language-select');
        const ttsConvertButton = document.getElementById('tts-convert-button');
        const ttsStatus = document.getElementById('tts-status');
        const ttsAudioPlayer = document.getElementById('tts-audio-player');
        const ttsOutputContainer = document.getElementById('tts-output-container');

        // Available voices for TTS
        const availableVoices = {
            'en-US': [
                { name: 'Kore (Firm)', value: 'Kore' },
                { name: 'Puck (Upbeat)', value: 'Puck' },
                { name: 'Zephyr (Bright)', value: 'Zephyr' },
                { name: 'Charon (Informative)', value: 'Charon' },
                { name: 'Fenrir (Excitable)', value: 'Fenrir' },
                { name: 'Leda (Youthful)', value: 'Leda' }
            ],
            'es-US': [
                { name: 'Callirrhoe (Easy-going)', value: 'Callirrhoe' },
                { name: 'Autonoe (Bright)', value: 'Autonoe' },
                { name: 'Enceladus (Breathy)', value: 'Enceladus' }
            ],
            'ja-JP': [
                { name: 'Umbriel (Easy-going)', value: 'Umbriel' },
                { name: 'Iapetus (Clear)', value: 'Iapetus' },
                { name: 'Algieba (Smooth)', value: 'Algieba' }
            ],
            'de-DE': [
                { name: 'Despina (Smooth)', value: 'Despina' },
                { name: 'Erinome (Clear)', value: 'Erinome' },
                { name: 'Algenib (Gravelly)', value: 'Algenib' }
            ],
            'hi-IN': [
                { name: 'Rasalgethi (Informative)', value: 'Rasalgethi' },
                { name: 'Laomedeia (Upbeat)', value: 'Laomedeia' },
                { name: 'Achernar (Soft)', value: 'Achernar' }
            ],
            'fr-FR': [
                { name: 'Alnilam (Firm)', value: 'Alnilam' },
                { name: 'Schedar (Even)', value: 'Schedar' },
                { name: 'Gacrux (Mature)', value: 'Gacrux' }
            ],
            'pt-BR': [
                { name: 'Pulcherrima (Forward)', value: 'Pulcherrima' },
                { name: 'Achird (Friendly)', value: 'Achird' },
                { name: 'Zubenelgenubi (Casual)', value: 'Zubenelgenubi' }
            ],
            'ru-RU': [
                { name: 'Vindemiatrix (Gentle)', value: 'Vindemiatrix' },
                { name: 'Sadachbia (Lively)', value: 'Sadachbia' },
                { name: 'Sadaltager (Knowledgeable)', value: 'Sadaltager' }
            ]
        };

        // Populate the voice selection dropdown
        function populateVoices() {
            ttsLanguageSelect.innerHTML = '';
            for (const lang in availableVoices) {
                const optgroup = document.createElement('optgroup');
                optgroup.label = lang;
                availableVoices[lang].forEach(voice => {
                    const option = document.createElement('option');
                    option.value = voice.value;
                    option.textContent = voice.name;
                    optgroup.appendChild(option);
                });
                ttsLanguageSelect.appendChild(optgroup);
            }
        }

        populateVoices();

        // Helper function to convert base64 PCM to a WAV blob
        function pcmToWav(pcmData, sampleRate) {
            const buffer = new ArrayBuffer(44 + pcmData.length * 2);
            const view = new DataView(buffer);

            // RIFF identifier
            writeString(view, 0, 'RIFF');
            // file length
            view.setUint32(4, 36 + pcmData.length * 2, true);
            // RIFF type
            writeString(view, 8, 'WAVE');
            // format chunk identifier
            writeString(view, 12, 'fmt ');
            // format chunk length
            view.setUint32(16, 16, true);
            // sample format (1 = PCM)
            view.setUint16(20, 1, true);
            // channel count
            view.setUint16(22, 1, true);
            // sample rate
            view.setUint32(24, sampleRate, true);
            // byte rate
            view.setUint32(28, sampleRate * 2, true);
            // block align
            view.setUint16(32, 2, true);
            // bits per sample
            view.setUint16(34, 16, true);
            // data chunk identifier
            writeString(view, 36, 'data');
            // data chunk length
            view.setUint32(40, pcmData.length * 2, true);

            // Write PCM data
            for (let i = 0; i < pcmData.length; i++, offset += 2) {
                view.setInt16(44 + i * 2, pcmData[i], true);
            }

            return new Blob([view], { type: 'audio/wav' });

            function writeString(view, offset, string) {
                for (let i = 0; i < string.length; i++) {
                    view.setUint8(offset + i, string.charCodeAt(i));
                }
            }
        }
        
        // Main TTS conversion function
        ttsConvertButton.addEventListener('click', async () => {
            const text = ttsTextInput.value.trim();
            const voiceName = ttsLanguageSelect.value;
            if (!text) {
                showModal('Please enter some text to convert!');
                return;
            }

            ttsStatus.textContent = 'Generating audio...';
            ttsStatus.style.color = '#93c5fd';
            ttsAudioPlayer.src = '';
            ttsOutputContainer.classList.add('hidden');
            
            try {
                const payload = {
                    contents: [{
                        parts: [{ text: text }]
                    }],
                    generationConfig: {
                        responseModalities: ["AUDIO"],
                        speechConfig: {
                            voiceConfig: {
                                prebuiltVoiceConfig: { voiceName: voiceName }
                            }
                        }
                    },
                    model: "gemini-2.5-flash-preview-tts"
                };

                const apiKey = "";
                const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-tts:generateContent?key=${apiKey}`;
                
                const response = await fetchWithRetry(apiUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                
                const result = await response.json();
                const part = result?.candidates?.[0]?.content?.parts?.[0];
                const audioData = part?.inlineData?.data;
                const mimeType = part?.inlineData?.mimeType;

                if (audioData && mimeType && mimeType.startsWith("audio/")) {
                    // MimeType is 'audio/L16;rate=24000'
                    const sampleRate = parseInt(mimeType.match(/rate=(\d+)/)[1], 10);
                    // Decode base64 to ArrayBuffer
                    const binaryString = atob(audioData);
                    const bytes = new Uint8Array(binaryString.length);
                    for (let i = 0; i < binaryString.length; i++) {
                        bytes[i] = binaryString.charCodeAt(i);
                    }
                    const pcm16 = new Int16Array(bytes.buffer);

                    const wavBlob = pcmToWav(pcm16, sampleRate);
                    const audioUrl = URL.createObjectURL(wavBlob);
                    
                    ttsAudioPlayer.src = audioUrl;
                    ttsOutputContainer.classList.remove('hidden');
                    ttsStatus.textContent = 'Audio generated. Press play to listen.';
                    ttsStatus.style.color = '#4ade80';
                } else {
                    throw new Error('Invalid audio data received from API.');
                }
                
            } catch (error) {
                console.error('Error generating TTS:', error);
                ttsStatus.textContent = 'Failed to generate audio. Please try again.';
                ttsStatus.style.color = '#f87171';
            }
        });

        // Helper function for PCM to WAV conversion
        function pcmToWav(pcm16, sampleRate) {
            const pcmData = pcm16.buffer;
            const buffer = new ArrayBuffer(44 + pcmData.byteLength);
            const view = new DataView(buffer);

            let offset = 0;
            // Write string helper
            const writeString = (str) => {
                for (let i = 0; i < str.length; i++) {
                    view.setUint8(offset + i, str.charCodeAt(i));
                }
                offset += str.length;
            };

            // RIFF identifier
            writeString('RIFF');
            // file length
            view.setUint32(offset, 36 + pcmData.byteLength, true); offset += 4;
            // RIFF type
            writeString('WAVE');
            // format chunk identifier
            writeString('fmt ');
            // format chunk length
            view.setUint32(offset, 16, true); offset += 4;
            // sample format (1 = PCM)
            view.setUint16(offset, 1, true); offset += 2;
            // channel count
            view.setUint16(offset, 1, true); offset += 2;
            // sample rate
            view.setUint32(offset, sampleRate, true); offset += 4;
            // byte rate
            view.setUint32(offset, sampleRate * 2, true); offset += 4;
            // block align
            view.setUint16(offset, 2, true); offset += 2;
            // bits per sample
            view.setUint16(offset, 16, true); offset += 2;
            // data chunk identifier
            writeString('data');
            // data chunk length
            view.setUint32(offset, pcmData.byteLength, true); offset += 4;
            
            // Write PCM data
            const pcmBytes = new Uint8Array(pcmData);
            for (let i = 0; i < pcmBytes.length; i++) {
                view.setUint8(offset + i, pcmBytes[i]);
            }

            return new Blob([view], { type: 'audio/wav' });
        }


        // ====================================================================
        // SPEECH-TO-TEXT (STT) LOGIC
        // ====================================================================
        const sttRecordButton = document.getElementById('stt-record-button');
        const sttStatus = document.getElementById('stt-status');
        const sttOutput = document.getElementById('stt-output');
        const sttPlaceholder = document.getElementById('stt-placeholder');

        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        let recognition;
        let isRecording = false;

        if (SpeechRecognition) {
            recognition = new SpeechRecognition();
            recognition.continuous = true;
            recognition.interimResults = true;
            recognition.lang = 'en-US'; // Set a default language

            recognition.onstart = () => {
                isRecording = true;
                sttStatus.textContent = 'Listening...';
                sttRecordButton.textContent = 'Stop Recording';
                sttRecordButton.classList.remove('from-red-600', 'to-red-800', 'hover:from-red-800', 'hover:to-red-600');
                sttRecordButton.classList.add('from-gray-500', 'to-gray-600', 'hover:from-gray-600', 'hover:to-gray-500');
            };

            recognition.onresult = (event) => {
                let interimTranscript = '';
                let finalTranscript = '';

                for (let i = event.resultIndex; i < event.results.length; ++i) {
                    const transcript = event.results[i][0].transcript;
                    if (event.results[i].isFinal) {
                        finalTranscript += transcript + ' ';
                    } else {
                        interimTranscript += transcript;
                    }
                }
                sttOutput.innerHTML = `<p class="text-gray-200">${finalTranscript} <span class="text-gray-400">${interimTranscript}</span></p>`;
                sttPlaceholder.style.display = 'none';
            };

            recognition.onend = () => {
                isRecording = false;
                sttStatus.textContent = 'Recording stopped.';
                sttRecordButton.textContent = 'Start Recording';
                sttRecordButton.classList.remove('from-gray-500', 'to-gray-600', 'hover:from-gray-600', 'hover:to-gray-500');
                sttRecordButton.classList.add('from-red-600', 'to-red-800', 'hover:from-red-800', 'hover:to-red-600');
                if (sttOutput.textContent.trim() === '') {
                    sttPlaceholder.style.display = 'block';
                }
            };

            recognition.onerror = (event) => {
                console.error('Speech recognition error:', event.error);
                sttStatus.textContent = `Error: ${event.error}`;
            };
            
        } else {
            sttStatus.textContent = 'Speech-to-Text not supported in this browser.';
            sttStatus.style.color = '#f87171';
            sttRecordButton.disabled = true;
        }

        sttRecordButton.addEventListener('click', () => {
            if (isRecording) {
                recognition.stop();
            } else {
                sttOutput.innerHTML = '';
                sttPlaceholder.style.display = 'block';
                recognition.start();
            }
        });


        // ====================================================================
        // PDF TEXT EXTRACTOR LOGIC
        // ====================================================================
        const pdfFileInput = document.getElementById('pdfFileInput');
        const convertPdfButton = document.getElementById('convert-pdf-button');
        const pdfStatus = document.getElementById('pdf-status');
        const pdfOutput = document.getElementById('pdf-output');
        const pdfPlaceholder = document.getElementById('pdf-placeholder');

        convertPdfButton.addEventListener('click', () => {
            const file = pdfFileInput.files[0];
            if (!file) {
                showModal('Please select a PDF file first!');
                return;
            }

            pdfStatus.textContent = 'Extracting text...';
            pdfStatus.style.color = '#93c5fd';
            pdfPlaceholder.style.display = 'none';
            pdfOutput.innerHTML = '';

            const fileReader = new FileReader();
            fileReader.onload = async function() {
                const typedarray = new Uint8Array(this.result);
                try {
                    const pdf = await pdfjsLib.getDocument({ data: typedarray }).promise;
                    let fullText = '';
                    
                    for (let i = 1; i <= pdf.numPages; i++) {
                        const page = await pdf.getPage(i);
                        const textContent = await page.getTextContent();
                        const pageText = textContent.items.map(item => item.str).join(' ');
                        fullText += pageText + '\n\n';
                    }

                    if (fullText.trim()) {
                        pdfOutput.innerHTML = `<p>${fullText.replace(/\n/g, '<br>')}</p>`;
                        pdfStatus.textContent = 'Extraction complete!';
                        pdfStatus.style.color = '#4ade80';
                    } else {
                        pdfOutput.innerHTML = `<p class="text-gray-400 italic">No text found in PDF.</p>`;
                        pdfStatus.textContent = 'PDF processed, but no text was extracted.';
                        pdfStatus.style.color = '#fbbf24';
                    }
                } catch (error) {
                    console.error('Error converting PDF:', error);
                    pdfStatus.textContent = 'Failed to extract text. Please ensure it is a valid PDF.';
                    pdfStatus.style.color = '#f87171';
                    pdfPlaceholder.style.display = 'block';
                }
            };
            fileReader.readAsArrayBuffer(file);
        });


        // ====================================================================
        // AI TEXT-TO-IMAGE LOGIC
        // ====================================================================
        const textToImagePrompt = document.getElementById('text-to-image-prompt');
        const generateImageButton = document.getElementById('generate-image-button');
        const textToImageStatus = document.getElementById('text-to-image-status');
        const generatedImage = document.getElementById('generated-image');
        const imagePlaceholder = document.getElementById('image-placeholder');

        generateImageButton.addEventListener('click', async () => {
            const prompt = textToImagePrompt.value.trim();
            if (!prompt) {
                showModal('Please enter a prompt to generate an image!');
                return;
            }

            textToImageStatus.textContent = 'Generating image...';
            textToImageStatus.style.color = '#93c5fd';
            generatedImage.classList.add('hidden');
            imagePlaceholder.classList.remove('hidden');
            imagePlaceholder.textContent = 'Generating...';

            try {
                const payload = { instances: { prompt: prompt }, parameters: { "sampleCount": 1 } };
                const apiKey = "";
                const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:predict?key=${apiKey}`;

                const response = await fetchWithRetry(apiUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                const result = await response.json();
                const base64Data = result.predictions?.[0]?.bytesBase64Encoded;

                if (base64Data) {
                    generatedImage.src = `data:image/png;base64,${base64Data}`;
                    generatedImage.classList.remove('hidden');
                    imagePlaceholder.classList.add('hidden');
                    textToImageStatus.textContent = 'Image generation complete!';
                    textToImageStatus.style.color = '#4ade80';
                } else {
                    throw new Error('Image data not found in response.');
                }
            } catch (error) {
                console.error('Error generating image:', error);
                textToImageStatus.textContent = 'Failed to generate image. Please try again.';
                textToImageStatus.style.color = '#f87171';
                imagePlaceholder.textContent = 'Image generation failed.';
                imagePlaceholder.classList.remove('hidden');
                generatedImage.classList.add('hidden');
            }
        });


        // ====================================================================
        // IMAGE-TO-ANIME STYLE LOGIC
        // ====================================================================
        const animeImageInput = document.getElementById('anime-image-input');
        const convertToAnimeButton = document.getElementById('convert-to-anime-button');
        const animeStatus = document.getElementById('anime-status');
        const animeOutputImage = document.getElementById('anime-output-image');
        const animePlaceholder = document.getElementById('anime-placeholder');

        convertToAnimeButton.addEventListener('click', async () => {
            const file = animeImageInput.files[0];
            if (!file) {
                showModal('Please select an image file to convert!');
                return;
            }

            animeStatus.textContent = 'Analyzing image...';
            animeStatus.style.color = '#93c5fd';
            animeOutputImage.classList.add('hidden');
            animePlaceholder.classList.remove('hidden');
            animePlaceholder.textContent = 'Analyzing...';
            
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onloadend = async () => {
                const base64Image = reader.result.split(',')[1];
                
                try {
                    // Step 1: Use Gemini to describe the image
                    const descriptionPrompt = `Describe this image in detail, focusing on style, subjects, and colors, so that a text-to-image model can recreate it in an anime style. Include specific artistic terms.`;
                    
                    const visionPayload = {
                        contents: [{
                            parts: [
                                { text: descriptionPrompt },
                                { inlineData: { mimeType: file.type, data: base64Image } }
                            ]
                        }]
                    };
                    
                    const visionApiKey = "";
                    const visionApiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key=${visionApiKey}`;
                    
                    const visionResponse = await fetchWithRetry(visionApiUrl, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(visionPayload)
                    });
                    
                    const visionResult = await visionResponse.json();
                    const description = visionResult.candidates?.[0]?.content?.parts?.[0]?.text;

                    if (!description) {
                        throw new Error('Failed to get image description from API.');
                    }
                    
                    animeStatus.textContent = 'Image analyzed. Generating anime version...';

                    // Step 2: Use the description to generate an anime image
                    const animePrompt = `Anime style, detailed, high-quality illustration of the following: "${description}"`;
                    
                    const imageGenPayload = { instances: { prompt: animePrompt }, parameters: { "sampleCount": 1 } };
                    const imageGenApiKey = "";
                    const imageGenApiUrl = `https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:predict?key=${imageGenApiKey}`;
                    
                    const imageGenResponse = await fetchWithRetry(imageGenApiUrl, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(imageGenPayload)
                    });
                    
                    const imageGenResult = await imageGenResponse.json();
                    const base64Data = imageGenResult.predictions?.[0]?.bytesBase64Encoded;

                    if (base64Data) {
                        animeOutputImage.src = `data:image/png;base64,${base64Data}`;
                        animeOutputImage.classList.remove('hidden');
                        animePlaceholder.classList.add('hidden');
                        animeStatus.textContent = 'Conversion complete!';
                        animeStatus.style.color = '#4ade80';
                    } else {
                        throw new Error('Anime image data not found in response.');
                    }
                } catch (error) {
                    console.error('Error converting image to anime:', error);
                    animeStatus.textContent = 'Failed to convert image. Please try again.';
                    animeStatus.style.color = '#f87171';
                    animePlaceholder.textContent = 'Conversion failed.';
                    animePlaceholder.classList.remove('hidden');
                    animeOutputImage.classList.add('hidden');
                }
            };
        });

        // ====================================================================
        // AUDIO PLAYER LOGIC
        // ====================================================================
        const audioFileInput = document.getElementById('audioFileInput');
        const audioPlayer = document.getElementById('audioPlayer');
        const audioStatus = document.getElementById('audio-status');

        audioFileInput.addEventListener('change', (event) => {
            const file = event.target.files[0];
            if (file) {
                const url = URL.createObjectURL(file);
                audioPlayer.src = url;
                audioStatus.textContent = `Audio file "${file.name}" loaded successfully.`;
                audioStatus.style.color = '#4ade80';
            } else {
                audioPlayer.src = '';
                audioStatus.textContent = 'No audio file selected.';
                audioStatus.style.color = '#f87171';
            }
        });

        // ====================================================================
        // TEXT-TO-VIDEO (UNSUPPORTED)
        // This is a placeholder as client-side text-to-video is not feasible.
        // The HTML already contains a message, so no JS logic is needed here.
        // ====================================================================

        /*
            ====================================================================
            *** END_YOUR_PROJECT_JAVASCRIPT ***
            ====================================================================
        */
    </script>
</body>
</html>
