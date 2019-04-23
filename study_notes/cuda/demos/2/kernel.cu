# include <iostream>
# include <cstdlib>

using namespace std;

__global__ void add(int a, int b, int *c) {
	*c = a + b;
}

int main(int argc, const char * const * argv)
{
	int a, b, c, *dev_c;

	if (argc != 3) {
		cout << "please input two numbers a and b." << endl;
		return 1;
	}

	a = atoi(argv[1]);
	b = atoi(argv[2]);

	cudaMalloc((void**)&dev_c, sizeof(int));

	add<<<1,1>>>(a, b, dev_c);

	cudaMemcpy(&c, dev_c, sizeof(int), cudaMemcpyDeviceToHost);
	cudaFree(dev_c);

	cout << a << "+" << b << "=" << c <<"." << endl;

	return 0;
}
