# -*- coding: utf-8 -*-

import os
import math
import matplotlib.pyplot as plt

from .colors_and_lines import Color

#%%============================================================================
def trim_img(
        files,
        white_margin=True,
        pad_width=20,
        pad_color='w',
        inplace=False,
        verbose=True,
        show_old_img=False,
        show_new_img=False,
        forcibly_overwrite=False,
        resize=False,
        resize_ratio=1.0,
):
    '''
    Trim the margins of image file(s) on the hard drive, and (optionally)
    add padded margins of a specified width and color.

    Parameters
    ----------
    files : str or list<str> or tuple<str>
        A file name (as Python str) or several file names (as Python list or
        tuple) to be trimmed.
    white_margin : bool
        Whether to treat white color as the margin to be trimmed. If ``True``,
        white image margins will be trimmed. If ``False``, black image margins
        will be trimmed.
    pad_width : float
        The amount of white margins to be padded (unit: pixels).
    pad_color : str or tuple<float> or list<float>
        The color of the padded margin. Valid ``pad_color`` values are color
        names recognizable by matplotlib: https://matplotlib.org/tutorials/colors/colors.html
    inplace : bool
        Whether or not to replace the existing figure file with the trimmed
        content.
    verbose : bool
        Whether or not to print the progress onto the console.
    show_old_img : bool
        Whether or not to show the old figure in the console.
    show_new_img : bool
        Whether or not to show the trimmed figure in the console.
    forcibly_overwrite : bool
        Whether or not to overwrite an image on the hard drive with the same
        name. Only applicable when ``inplace`` is ``False``.
    resize : bool
        Whether to resize the padded image
    resize_ratio : float
        The image resizing ratio.  It has no effect if ``resize` is false.
        For example, if it's 0.5, it means resizing to 50% of the original
        width and height.
    '''
    try:
        import PIL
        import PIL.ImageOps
        from PIL import Image
    except ImportError:
        raise ImportError(
            '\nPlease install PIL in order to use `trim_img()`.\n'
            'Install with conda (recommended):\n'
            '    >>> conda install PIL\n'
            'To install without conda, refer to:\n'
            '    http://www.pythonware.com/products/pil/'
        )

    if not isinstance(files,(list,tuple)):
        files = [files]

    pad_width = int(pad_width)

    for filename in files:
        if verbose:
            print('Trimming %s...' % filename)
        im0 = PIL.Image.open(filename)  # load image
        im1 = im0.convert('RGB')  # convert from RGBA to RGB
        if white_margin:
            im1 = PIL.ImageOps.invert(im1)  # invert color to have black margin

        if show_old_img:
            plt.imshow(im0)
            plt.xticks([])
            plt.yticks([])

        im2 = im1.crop(im1.getbbox())  # crop the black-color margin
        if white_margin:
            im2 = PIL.ImageOps.invert(im2)  # invert the color back

        pad_color_rgb = Color(pad_color).as_rgb(normalize=False)
        im3 = PIL.ImageOps.expand(im2, border=pad_width, fill=pad_color_rgb)

        if resize:
            new_width = im3.width
            new_height = im3.height
            im3 = im3.resize((new_width, new_height), Image.ANTIALIAS)

        if show_new_img:
            plt.imshow(im3)
            plt.xticks([])
            plt.yticks([])

        if not inplace:
            filename_without_ext, ext = os.path.splitext(filename)
            new_filename_ = '%s_trimmed%s' % (filename_without_ext, ext)

            if not os.path.exists(new_filename_):
                im3.save(new_filename_)
                if verbose:
                    print('  New file created: %s' % new_filename_)
            else:
                if forcibly_overwrite:
                    im3.save(new_filename_)
                    if verbose:
                        print('  Overwriting existing file: %s' % new_filename_)
                else:
                    print('  New file is not saved, because a file with the '
                          'same name already exists at "%s".' % new_filename_)
        else:
            im3.save(filename)
            if verbose:
                print('  Original image file overwritten.')

#%%============================================================================
def pad_img(
        files, target_aspect_ratio=1.0, pad_color='white', inplace=False,
        verbose=True, show_old_img=False, show_new_img=False,
        forcibly_overwrite=False, resize=False, new_width_height=(640, 480),
):
    """
    Pad empty edges to images so that they meet the target aspect ratio (i.e.,
    more square).

    Parameters
    ----------
    files : str or list<str> or tuple<str>
        A file name (as Python str) or several file names (as Python list or
        tuple) to be padded.
    target_aspect_ratio : float
        The target aspect ratio to convert the original image into. A value
        between 0 (exclusive) and 1 (inclusive).
    pad_color : str or tuple<float> or list<float>
        The color of the padded margin. Valid ``pad_color`` values are color
        names recognizable by matplotlib: https://matplotlib.org/tutorials/colors/colors.html
    inplace : bool
        Whether or not to replace the existing figure file with the padded
        content.
    verbose : bool
        Whether or not to print the progress onto the console.
    show_old_img : bool
        Whether or not to show the old figure in the console.
    show_new_img : bool
        Whether or not to show the padded figure in the console.
    forcibly_overwrite : bool
        Whether or not to overwrite an image on the hard drive with the same
        name. Only applicable when ``inplace`` is ``False``.
    resize : bool
        Whether to resize the padded image
    new_width_height : (int, int)
        The new image width and height.  It has no effect if ``resize` is false,
        and there will be an error if the provided aspect ratio doesn't match
        ``target_aspect_ratio``.
    """
    try:
        import PIL
        import PIL.ImageOps
        from PIL import Image
    except ImportError:
        raise ImportError(
            '\nPlease install PIL in order to use `trim_img()`.\n'
            'Install with conda (recommended):\n'
            '    >>> conda install PIL\n'
            'To install without conda, refer to:\n'
            '    http://www.pythonware.com/products/pil/'
        )

    if target_aspect_ratio > 1.0 :
        raise ValueError('`target_aspect_ratio` should be <= 1.0.')

    if not isinstance(files,(list,tuple)):
        files = [files]

    for filename in files:
        if verbose:
            print('Padding %s...' % filename)

        im0 = PIL.Image.open(filename)  # load image

        if show_old_img:
            plt.imshow(im0)
            plt.xticks([])
            plt.yticks([])

        width = im0.size[0]
        height = im0.size[1]

        print(f'Original image resolution: {width} x {height}')

        if width >= height:  # landscape layout
            print('Input image is in landscape layout')
            if width * target_aspect_ratio > height:  # image too wide
                print('Image too wide')
                padded_width = width
                padded_height = width * target_aspect_ratio
                pad_length_single_side = int(padded_height - height) // 2
                upper_left_corner_coord = (0, pad_length_single_side)
            else:
                print('Image too narrow')
                padded_height = height
                padded_width = height / target_aspect_ratio
                pad_length_single_side = int(padded_width - width) // 2
                upper_left_corner_coord = (pad_length_single_side, 0)
            # END IF
        else:  # portrait layout
            print('Input image is in portrait layout')
            if height * target_aspect_ratio > width:  # image too narrow
                print('Image too narrow')
                padded_height = height
                padded_width = height * target_aspect_ratio
                pad_length_single_side = int(padded_width - width) // 2
                upper_left_corner_coord = (pad_length_single_side, 0)
            else:
                print('Image too wide')
                padded_width = width
                padded_height = width / target_aspect_ratio
                pad_length_single_side = int(padded_height - height) // 2
                upper_left_corner_coord = (0, pad_length_single_side)
            # END IF
        # END IF

        new_img_size = (int(padded_width), int(padded_height))
        pad_color_rgb = Color(pad_color).as_rgb(normalize=False)
        im1 = PIL.Image.new('RGB', new_img_size, color=pad_color_rgb)
        im1.paste(im0, box=upper_left_corner_coord)

        print(f'After padding: {new_img_size}')

        if resize:
            new_width, new_height = new_width_height
            shorter_side = min(new_width, new_height)
            longer_side = max(new_width, new_height)
            if not math.isclose(shorter_side / longer_side, target_aspect_ratio):
                raise ValueError('The new dimension must match `target_aspect_ratio`')

            im1 = im1.resize((new_width, new_height), Image.ANTIALIAS)

        if show_new_img:
            plt.imshow(im1)
            plt.xticks([])
            plt.yticks([])

        if not inplace:
            filename_without_ext, ext = os.path.splitext(filename)
            new_filename_ = '%s_padded%s' % (filename_without_ext, ext)

            if not os.path.exists(new_filename_):
                im1.save(new_filename_)
                if verbose:
                    print('  New file created: %s' % new_filename_)
            else:
                if forcibly_overwrite:
                    im1.save(new_filename_)
                    if verbose:
                        print('  Overwriting existing file: %s' % new_filename_)
                else:
                    print('  New file is not saved, because a file with the '
                          'same name already exists at "%s".' % new_filename_)
        else:
            im1.save(filename)
            if verbose:
                print('  Original image file overwritten.')
