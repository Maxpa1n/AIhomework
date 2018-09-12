package homework2;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

/**
 * 选择出html文件中的URL链接
 * @author Administrator
 *
 */


public class PickURL {
	public static void main(String[] args) {
		
		String xmlString;
		String path = "F:/Users/Administrator/workspace/homework2/src/homework2/sina.html";
		
		byte[] strBuffer = null;
		int flen = 0;
		File xmlfile = new File(path);
		try {
		InputStream in = new FileInputStream(xmlfile);
		flen = (int)xmlfile.length();
		strBuffer = new byte[flen];
		in.read(strBuffer, 0, flen);
		} catch (FileNotFoundException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
		} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
		}
		xmlString = new String(strBuffer);
		//System.out.print(xmlString);
		
		
		
		
		
		  
	        String[] sourceStrArray = xmlString.split("href=\"");
	        for (int i = 0; i < sourceStrArray.length; i++) 
	        {
	            //System.out.println(sourceStrArray[i]);
	            //System.out.println("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@");
	        }
	       
	        for(int j = 1;j < sourceStrArray.length; j++)
	        {
	        	String[] UrlStrArray = sourceStrArray[j].split("\"");
	        	//System.out.println(UrlStrArray.length);
	        	System.out.println(UrlStrArray[0]);
	        	
	        }
	    
	  }

}
