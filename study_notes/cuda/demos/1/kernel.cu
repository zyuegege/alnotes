# include <iostream>


__global__ void kernel(void) {
}

int main(void)
{
	kernel<<<1,1>>>();
	std::cout << "hello world" << std::endl;
	return 0;
}
