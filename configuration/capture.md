# Capture
The capture node contains information relevant to capturing screenshots from an SGCT application.

- `path` **[string]** _optional_

  Sets the path used when creating screenshots. The default value is to use the current working directory.

- `format` **[(png, PNG, tga, TGA, jpg, or JPG)]** _optional_

  Sets the screenshot format that should be used for the screenshots taken of the application. The default value is `PNG`.

- `range-begin` **[int > 0]** _optional_

  The index of the first screenshot that will actually be rendered. If this value is set, all previous screenshots will be ignored, but the counter will be increased either way. If this value is set, the `range-end` value also needs to be set. A value of `-1` will mean the same thing as `0`, saying the everything from the first frame will be captured, which is also the default.

- `range-end` **[int > 0]** _optional_

  The index of the last screenshot that will *not* be rendered anymore. If this value is set, all screenshots starting with this index will be ignored. If this value is set, the `range-begin` value also needs to be set. A value of `-1` will mean that all remaining screenshots will be captured, which is the default.
