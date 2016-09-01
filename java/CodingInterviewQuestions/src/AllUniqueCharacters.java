/**
 * 
 */

/**
 * @author sourav
 *
 */
public class AllUniqueCharacters {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String test = "thisisastring";
		System.out.println(ifAllUniqueCharatersNoExtraSpace(test));

	}
	
	public static boolean ifAllUniqueCharaters(String str){
		boolean[] items = new boolean[26];
		int strLength = str.length();
		for(int i=0;i<strLength;i++){
			int currentCharValue = str.charAt(i)-'a';
			if(items[currentCharValue])
				return false;
			else
				items[currentCharValue]= true; 
		}
		return true;
	}

	public static boolean ifAllUniqueCharatersNoExtraSpace(String str){
		int strLength = str.length();
		int checker = 0;
		for(int i=0;i<strLength;i++){
			int currentCharValue = str.charAt(i)-'a';
			//System.out.println(Integer.toBinaryString(1<<currentCharValue));
			if((checker & (1<<currentCharValue)) > 0)
				return false;
			else
				checker = checker | (1<<currentCharValue);
		}
		return true;
	}

}
