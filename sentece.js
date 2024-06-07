class TrieNode {
    constructor() {
        this.children = {};
        this.isEndOfWord = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    insert(word) {
        let node = this.root;
        for (const char of word) {
            if (!node.children[char]) {
                node.children[char] = new TrieNode();
            }
            node = node.children[char];
        }
        node.isEndOfWord = true;
    }

    searchRoot(word) {
        let node = this.root;
        let prefix = "";
        for (const char of word) {
            if (node.isEndOfWord) {
                return prefix;
            }
            if (!node.children[char]) {
                return word;
            }
            prefix += char;
            node = node.children[char];
        }
        return node.isEndOfWord ? prefix : word;
    }
}

function replaceWords(dictionary, sentence) {
    const trie = new Trie();

    // Insert all roots into the Trie
    for (const root of dictionary) {
        trie.insert(root);
    }

    // Split the sentence into words and replace each word
    const words = sentence.split(" ");
    for (let i = 0; i < words.length; i++) {
        words[i] = trie.searchRoot(words[i]);
    }

    // Join the words back into a sentence
    return words.join(" ");
}

// Example usage
const dictionary1 = ["cat", "bat", "rat"];
const sentence1 = "the cattle was rattled by the battery";
console.log(replaceWords(dictionary1, sentence1)); // Output: "the cat was rat by the bat"

const dictionary2 = ["a", "b", "c"];
const sentence2 = "aadsfasf absbs bbab cadsfafs";
console.log(replaceWords(dictionary2, sentence2)); // Output: "a a b c"
