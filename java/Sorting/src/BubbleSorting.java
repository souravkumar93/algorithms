
public class BubbleSorting {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {2,3,4,5,6,2,3,4,5,5,2,2,3,3,4,5};
		arr = bubbleSort(arr);
		printArray(arr);
	}
	
	public static int[] bubbleSort(int[] arr){
		boolean swap;
		for(int i = arr.length-1;i>0;i--){
			swap = false;
			for(int j=0;j<i;j++){
				if(arr[j]>arr[j+1]){
					int temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
					swap = true;
				}
			}
			if(!swap)
				return arr;
		}		
		return arr;
	}
	
	public static void printArray(int[] arr){
		for(int i=0;i<arr.length;i++){
			System.out.println(arr[i]);
		}
	}

}
