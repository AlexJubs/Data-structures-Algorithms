
//  Calculating mean 
double mean(int a[]) 
{ 
	int n = std::size(a)/std::size(a[0]);
    int sum = 0;
    for (int i = 0; i < n; i++) sum += a[i]; 
    double output = sum/n
    return output; 
} 
  
// Calculating median 
double findMedian(int a[], int n) 
{ 
	int n = std::size(a)/std::size(a[0]);
    sort(a, a+n); 
    double output;

    if (n % 2 != 0) 
    	output = a[n/2];
    	return output;

    // if the length of the array is not even
    output = (a[(n-1)/2] + a[n/2])/2.0  
    return output; 
} 