<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bangla Word Miner</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-800 flex items-center justify-center h-screen">
    <div class="bg-gray-200 p-8 rounded-lg shadow-lg w-full max-w-xl">
        <h2 class="text-2xl font-bold mb-6 text-center">Bangla Word Miner</h2>
        <form action="{{ route("mine-words") }}" method="POST">
            @csrf
            <div class="mb-4">
                <label for="textbox" class="block text-gray-700 text-sm font-bold mb-2">Enter Text:</label>
                <textarea name="text" id="textbox" class="shadow-xl border border-amber-600 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" rows="10"></textarea>
            </div>
            <div class="flex items-center justify-center">
                <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Send</button>
            </div>
        </form>
    </div>
</body>
</html>