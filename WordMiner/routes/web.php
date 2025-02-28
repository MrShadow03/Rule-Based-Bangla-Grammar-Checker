<?php

use App\Http\Controllers\WordController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::post('/mine-words', [WordController::class, 'mineWords'])->name('mine-words');
Route::get('/words', [WordController::class, 'index']);
