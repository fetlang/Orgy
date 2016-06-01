#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int int_exp(int b, int e){
	int r=1;
	for(int i=0;i<e;i++){
		r*=b;
	}
	return r;
}

int closest_root(int b, int r){
	bool take_inverse = false;
	if (r<0){
		take_inverse = true;
		r=-r;
	}
	if(b<0 && r%2==0){
		fprintf(stderr, "Imaginary Root Error");
	}
	
	// At this point, r is positive
	int max = b;
	int min = 0;
	if(b<0){
		max = 0;
		min = b;
	}
	max++;
	min--;
	// Now start algorithm
	int n = (max+min)/2;
	int d;
	while (max-min>1){
		n =(max+min)/2;
		if(int_exp(n,r)>b){
			max = n;
		}else if(int_exp(n,r)==b){
			return n;
		}else{
			min = n;
		}
	}
	return n+1n;
}

int main(){
	for (int i=0;i<100;i++){
		printf("sqrt(%d)=%d\n",i,closest_root(i,2));
	}
	return 0;
}