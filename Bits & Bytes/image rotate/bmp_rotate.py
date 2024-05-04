if __name__ == "__main__":
    with open( "teapot.bmp", mode="rb") as read_file:
        read_file.seek( 10)
        pa_offset = int.from_bytes(read_file.read(4), byteorder="little")
        read_file.seek( 0)
        header = read_file.read( pa_offset)
        bmp_pixel_width = int.from_bytes(header[18:22], byteorder="little")
        bmp_pixel_height = int.from_bytes(header[22:26], byteorder="little")
        bits_per_pixel = int.from_bytes(header[28:30], byteorder="little")
        print( 
            "width: {0}, height: {1}, bpp: {2}"
            .format( bmp_pixel_width, bmp_pixel_height, bits_per_pixel)
        )
        read_file.seek( pa_offset) #skip bmp headers and capture raw image data
        pixel_array = bytearray( read_file.read())

        pixel_array_2d = []
        pixel_array_flat = bytearray()

        for col in range(bmp_pixel_height):
            for row in range(bmp_pixel_width):
                new_col = row
                new_row = bmp_pixel_width - col - 1
                pixel_loc = new_col * bmp_pixel_height * 3 + new_row * 3
                pixel_array_2d.append( pixel_array[pixel_loc:pixel_loc+3])

        for array in pixel_array_2d:
            pixel_array_flat.extend( array)

    with open( "newteapot.bmp", "wb") as write_file:
        write_file.write( header)
        write_file.write( pixel_array_flat)