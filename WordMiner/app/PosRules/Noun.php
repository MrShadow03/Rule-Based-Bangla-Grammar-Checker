<?php 

namespace App\PosRules;

class Noun {
    public function isNoun($sentence, $word): bool{
        $words = explode(' ', $sentence);
        return $this->determinerRule($words, $word) || $this->suffixRule($word);
    }

    protected function determinerRule($words, $word): bool {
        $determiners = config('grammar.determiner');
        $previousWord = $words[array_search($word, $words) - 1] ?? null;
        return in_array($previousWord, $determiners);
    }

    protected function suffixRule($word): bool {
        $suffixes = config('grammar.noun_suffix');
        
        //check if the suffix appear at the end of the word
        foreach ($suffixes as $suffix) {
            if (substr($word, -strlen($suffix)) === $suffix) {
                return true;
            }
        }
        return false;
    }

}




?>