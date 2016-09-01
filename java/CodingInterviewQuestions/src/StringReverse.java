/**
 * 
 */

/**
 * @author sourav
 *
 */
public class StringReverse {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		StringBuilder str = new StringBuilder("helloo");
		int end = str.length() - 1;
		for(int i=0;i<end;++i,--end){
			char temp = str.charAt(i);
			str.setCharAt(i, str.charAt(end));
			str.setCharAt(end, temp);
		}
		System.out.println(str);
	}
}
