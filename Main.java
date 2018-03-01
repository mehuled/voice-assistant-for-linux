import java.io.*;
import java.util.*;
import java.lang.*;

public class Main
{
    public static void main(String[] args) throws Exception
    {
    	System.out.println("Wait for atleast 20 sec to show the results.\n Results will vary accoding to number of files and processor of operating computer.\n");
	String command1 = "ls -lR | grep '^-' | sort -k 5 -rn | head -n 10";
	String command2 = "ls -lR > output.txt";
	
    	Process child = Runtime.getRuntime().exec(new String[] { "bash", "-c", command1 });
    	child.waitFor();
    	
    	// Get output stream to write from it
    	Scanner reader = new Scanner(new InputStreamReader(child.getInputStream()));
    	reader.useDelimiter("\r\n");
    	String line = "";
    	
    	
    	
    	while (reader.hasNext()) {
    		System.out.println(reader.nextLine());
	}
    }
}
