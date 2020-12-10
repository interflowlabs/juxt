# Juxt

[Juxt](https://juxt.io) is the simplest and easiest way to compare structured data. All you have to do is: 
-	Upload your data files
-	Configure the columns you want to compare (or ignore) and the key(s) to use
-	Submit the comparison and see the results
-	Share the results with others

This page will serve as the home for the Juxt documentation and issue tracking. 

If you would like to contact us, send an email to team@juxt.io.

# Juxt Configuration 
The Juxt Configuration is a JSON formatted document with the following properties:
-	name – String – The name of the comparison. This will show up above the comparison results.
-	description – String – A more detailed description of the comparison. This can include information or notes about the data files that are being compared. 
-	key_columns – Array of Strings – The column(s) to use for matching rows from each data file
-	side1_name – String – A display name for the side1 file. 
-	side2_name – String - A display name for the side2 file.
-	ignore_extra_columns – true/false – This tells Juxt to ignore columns that are not in both side1 and side2 files. 
-	isPublic – true/false - This value determines if your Juxt results are public to everyone. Default is false. 

Here is an example configuration: 
```{
  "name": "My First Juxt",
  "description": "This is my first Juxt. It’s just an example.",
  "key_columns": [
    "Column1"
  ],
  "ignore_columns": [
    "Column2"
  ],
  "side1_name": "Original",
  "side2_name": "New",
  "ignore_extra_columns": false,
  "isPublic": true
}```

