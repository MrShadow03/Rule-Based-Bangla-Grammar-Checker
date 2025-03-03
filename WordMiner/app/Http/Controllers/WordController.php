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

    private function detect_missing_words($words) {
        // Open file and read words into an associative array for fast lookup
        $word_dict = [];
        $handle = fopen(asset("data/dictionary/correct-words.txt"), "r");
        if ($handle) {
            while (($line = fgets($handle)) !== false) {
                $word = trim($line); // Remove extra spaces or newlines
                $word_dict[$word] = true; // Store in hash table for O(1) lookup
                dd($word);
            }
            fclose($handle);
        } else {
            die("Error opening file!");
        }
    
        // Check for missing words
        $missing_words = array_filter($words, function($word) use ($word_dict) {
            return !isset($word_dict[$word]);
        });
        dd($missing_words);
        return $missing_words;
    }
}
