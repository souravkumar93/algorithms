
public class QuickSorting {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {23,45,76,89,12,42,90,45};
		quickSort(arr, 0, arr.length-1);
		printArray(arr);
	}
	
	public static int partition(int[] arr, int low, int high){
		int temp,i,j;
		j=high;
		i=low+1;
		int pivot = arr[low];
		while(i<=j){
			while(arr[i]<pivot && i < high)
				i++;
			while(arr[j]>pivot)
				j--;
			if(i<j){
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
				i++;
				j--;
			}else
				i++;
		}
		arr[low] = arr[j];
		arr[j] = pivot;
		return j;
	}
	
	public static void quickSort(int[] arr,int low, int high){
		int pivot;
		if(low>=high){
			return;
		}
		pivot = partition(arr,low,high);
		quickSort(arr, low, pivot-1);
		quickSort(arr, pivot+1, high);
	}
	
	public static void printArray(int[] arr){
		for(int i=0;i<arr.length;i++){
			System.out.println(arr[i]);
		}
	}

}
