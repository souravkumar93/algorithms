/**
 * 
 */

/**
 * @author sourav
 *
 */
public class SelectionSort {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int[] arr = {9005,6,7,8,2,3,4,905,6};
		arr = SelectionSorting(arr);
		printArray(arr);
	}
	
	public static int[] SelectionSorting(int[] arr){
		int min;
		for(int i = 0;i<arr.length;i++){
			min = i;
			for(int j=i;j<arr.length;j++){
				if(arr[min]>arr[j]){
					min = j;
				}
			}
			if(i != min){
				int temp = arr[i];
				arr[i] = arr[min];
				arr[min] = temp;
			}
		}		
		return arr;
	}
	
	public static void printArray(int[] arr){
		for(int i=0;i<arr.length;i++){
			System.out.println(arr[i]);
		}
	}

}
