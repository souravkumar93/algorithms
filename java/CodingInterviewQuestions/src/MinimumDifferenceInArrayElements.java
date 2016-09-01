/**
 * 
 */

/**
 * @author sourav
 *
 */
public class MinimumDifferenceInArrayElements {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {1,2,9,15};
		//arr= normalizeArray(arr);
		int minDifference = getMinimum(arr);		
		System.out.println(minDifference);
	}
	
	public static int getMinimum(int[] arr){
		int checker = 0;
		int min = -1;
		for(int i=0;i<arr.length;i++){
			if((checker & (1<<arr[i]))>0)
				return 0;
			else{
				checker |= 1<<arr[i];
			}
		}
		
		return findMinDistance(checker);
	}
	
	public static int findMinDistance(int num){
		int minLength = 100000;		
		String str = Integer.toBinaryString(num);
		int count= 0;
		System.out.println(str);
		//while()
		return minLength;
	}
	
	public static int[] normalizeArray(int[] arr){
		int min = 0;
		for(int i=0;i<arr.length;i++){
			if(arr[min]>arr[i])
				min= i;
		}
		System.out.println(min);
		for(int i=0;i<arr.length;i++)
			arr[i] -= arr[min];
	
		return arr;
	}

}
