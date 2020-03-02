import sys
import numpy

def apply_filter(img_matrix, filter_size):
    print("Start Median Filtering " + str(filter_size)+"X"+str(filter_size))
    filtered_matrix = img_matrix[:]
    # TODO add your code here
    for i in range(0,len(img_matrix)-filter_size):
        print("Progress: "+ str(i) + " from "+str(len(img_matrix)))
        for j in range(0,len(img_matrix[0])-filter_size):
            block = numpy.array(img_matrix)[i:i+filter_size, j:j+filter_size]
            m = numpy.median(block)
            filtered_matrix[i][j] = int(m)

    return filtered_matrix

def read_ppm(input):
    with open(input, 'r') as f:
        magic_number = f.readline()
        comment = f.readline()
        size = f.readline().split()
        max_val = f.readline()
        width, height = int(size[0]), int(size[1])
        img_matrix = [[0 for j in range(width)] for i in range(height)]
        for i in range(height):
            pixel_row = f.readline().split()
            for j, pixel in enumerate(pixel_row):
                img_matrix[i][j] = int(pixel)
        return img_matrix


def write_ppm(output, img_matrix):
    width = len(img_matrix[0])
    height = len(img_matrix)
    with open(output, 'w') as fw:
        fw.write('P2\n')
        fw.write(
            '# Image from: https://homepages.inf.ed.ac.uk/rbf/HIPR2/median.htm\n'
        )
        fw.write('%d %d\n' % (width, height))
        fw.write('255\n')
        for img_row in img_matrix:
            for pixel in img_row:
                fw.write('%d ' % pixel)
            fw.write('\n')


def main():
    if len(sys.argv) < 4:
        print('Usage: python %s <input_file> <output_file> <filter_size>' %
              sys.argv[0])
        return
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    filter_size = int(sys.argv[3])
    img_matrix = read_ppm(input_file)
    flt_matrix = apply_filter(img_matrix, filter_size)
    write_ppm(output_file, flt_matrix)


if __name__ == '__main__':
    main()
    print("Filtering Done")
