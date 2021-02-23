import java.util.*;
import java.io.*;
import java.nio.Buffer;
import java.nio.file.Files;

class vigenere {
   
    public static String charFixer(String c){

    for (int i = 0; i < c.length(); i++){
        
        char current = c.charAt(i);

        if (current >= 'A' && current < 'Z'){
           c = c.replace(current, (char) (current + 32));
            //replaces to lowercase
        }


        else if (current < 'a' || current > 'z'){
           c = c.replace(current, '.');
           //nullifies character
            
        }

    }

    String finalPhrase = "";

    //filters "nullified" characters

    for (int i = 0; i < c.length();i++){
        if (c.charAt(i) != '.'){
            finalPhrase += c.charAt(i);
        }
    }

    return finalPhrase;
       

    }

    

    public static char[] readText(File f) {

        // convert uppercase to lowercase, and skip over any symbol or space

            try{

                char[] buffer = new char[512];

                BufferedReader read = new BufferedReader(new FileReader(f));
                StringBuilder build = new StringBuilder();

                String currline = read.readLine();


                while (currline != null){

                    currline = currline.replaceAll(" ", "");

                    currline = charFixer(currline);

                    build.append(currline);

                    currline = read.readLine();

                }

                

                for (int i = 0; i < build.toString().length(); i++){

                    buffer[i] = build.toString().charAt(i);
            
                }


                read.close();
                
                return buffer;

            }

            catch(IOException e){
                System.out.println("ERROR IN READING FILE: CHECK DIRECTORY");
            }

            return new char[0];

    }

    public static char[] encrypt (char[] plaintext, char[] keytext){

        char[] cipherText = new char[512];

        char[][] table = new char[26][26];

        for (int i = 0; i < 26; i++){
            for (int j = 0; j < 26; j++){
                table[i][j] = (char) (('a' + ((j+i)%26)));
            }
        }

        for (int i = 0; i < 512; i++){

            cipherText[i] = table[(int)plaintext[i] - 97][(int)keytext[i] - 97];

        }

        return cipherText;



    }

    public static void print(String s){

        for (int i = 0, buffer = s.length(); i < buffer; i += 80)
            //formats 80 characters per line
             System.out.println(s.substring(i, Math.min(i + 80, buffer)));

    }
    
    public static void main(String[] args) {
  
       File keyfile = new File (args[0]);
       File encryptfile = new File (args[1]);


        char[] plainString = new char[512];
        char[] keyString = new char[512];
        
        plainString = readText(encryptfile);

        keyString = readText(keyfile);

        for (int i = 0; i < 512; i++){
            if ((plainString[i] > 'z') || (plainString[i] < 'a')){
                plainString[i] = 'x';
            }
        }

        System.out.println("\nVigenere Key:\n");
        print(String.valueOf(keyString));

        int count = 0;

        for (int i = 0; i < 512; i++){
            if ((keyString[i] > 'z') || (keyString[i] < 'a')){
                break;
            }

        count++;

        }

        int i = count;

        while (i < 512){

            keyString[i] = keyString[i % count];
            i++;

        }
        
        
      
        System.out.println("Plaintext:\n\n");
        print(String.valueOf(plainString));
        
       
        System.out.println("\nCiphertext:\n");
        print(String.valueOf(encrypt(plainString, keyString)));



    }




}