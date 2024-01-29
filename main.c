#include <stdio.h>

int * bubble_soort(int len, int array[]) {
    for(int i = 0; i < len; i++) {
        for(int j = i+1; j < len; j++) {
            if(array[j] < array[i] ) {
                int tmp  = array[i];
                array[i] = array[j];
                array[j] = tmp;
            }
        }
    }
    return  array;
}

float average2(int len, int array[]) {
    int sum;
    for(int i = 0; i < len; i++) {
        sum += array[i];
    }
    return sum / (float) len;
}

float aver(int len, int array[]) {
  int sum;
  for(int i = 0; i < len; i++) {
    sum += array[i];
  }
  return sum / (float) len;
}

int * bubble_sort(int len, int array[]) {
  for(int i = 0; i < len; i++) {
    for(int j = i+i; j < len; j++) {
      if(array[j] < array[i]) {
        int tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
      }
    }
  }
  return array;
}

int main() {
    int num1, num2;
    num1 = 1;
    num2 = 2;
    int array[] = {num1, num2}; 
    int *sorted = bubble_soort(2, array);
    printf("%p", **sorted);
}


