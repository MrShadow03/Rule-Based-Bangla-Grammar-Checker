<?php

namespace App\Http\Controllers;

use App\Http\Requests\WordRequest;
use App\PosRules\Noun;
use Illuminate\Http\Request;

class WordController extends Controller
{
    public function mineWords(WordRequest $request)
    {
        $text = $this->cleanText($request->input('text'));

        $sentences = explode('।', $text);

        $nouns = [];

        foreach ($sentences as $key => $sentence) {
            $words = explode(' ', $sentence);
            foreach ($words as $word) {
                $noun = new Noun();
                if ($noun->isNoun($sentence, $word)) {
                    $nouns[] = $word;
                }
            }
            
            $sentences[$key] = implode(' ', $words);
        }

        dd($nouns);
        
    }

    private function cleanText($text)
    {
        $text = trim($text);

        // Remove all the punctuation from the text
        $punctuation = ['.', ',', '!', '?', ';', ':', '"', "'", '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+', '~', '`', '‘', '’', '“', '”', '…'];
        $text = str_replace($punctuation, '', $text);

        // Remove all the extra spaces from the text
        $text = preg_replace('/\s+/', ' ', $text);

        return $text;
    }
}
