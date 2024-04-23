import cv2

def convert_to_black_and_white(input_image_path, output_image_path):
    # Read the input image
    image = cv2.imread(input_image_path)

    # Check if the image was successfully loaded
    if image is None:
        return None

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite(output_image_path, grayscale_image)

    return output_image_path