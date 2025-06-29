def calculateDistance(color1, color2):
    """
        Calculate the distance between two colors in RGB space.
        Args:
            color1 (tuple): RGB values of the first color.
            color2 (tuple): RGB values of the second color.
        Returns:
            float: The Euclidean distance between the two colors.
    """
    return  ((color1[0] - color2[0]) ** 2 + (color1[1] - color2[1]) ** 2 + (color1[2] - color2[2]) ** 2) ** 0.5  


if __name__ == "__main__":
    # Example usage
    red = (255, 0, 0)
    green = (0, 255, 0)
    pink = (255, 192, 203)
    # Calculate distance between red and green
    distance = calculateDistance(red, green)
    print(f"The distance between {red} and {green} is: {distance}")

    # Calculate distance between red and pink
    distance = calculateDistance(red, pink) 
    print(f"The distance between {red} and {pink} is: {distance}")

    # Calculate distance between green and pink
    distance = calculateDistance(green, pink)
    print(f"The distance between {green} and {pink} is: {distance}")

    # Find the color closest to red
    colors = [green, pink]
    closest_color = min(colors, key=lambda color: calculateDistance(red, color))
    print(f"The color closest to {red} is: {closest_color}")
