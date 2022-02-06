import subprocess

def cri(cmd):
    subprocess.call(cmd, shell=True);

print("\x1b[1;37mE.G: site.com (\x1b[1;32mNO ENDING SLASH\x1b[1;37m) MUST BE NAME.EXTENSION")
domain = raw_input("\x1b[1;37mEnter Your Domain: \x1b[1;36m")
print("\x1b[1;37mFiles are stored here! (\x1b[1;32me.g: myfiles or rich\x1b[1;37m) output will be: \x1b[1;36mhttps://site.com/folder/file.extension")
uploadDir = raw_input("\x1b[1;37mEnter Desired Upload_Directory: \x1b[1;36m")
print("\x1b[1;37mThis is generally for fileNameLength (\x1b[1;32me.g: 12345.txt or 1laosori.txt\x1b[1;37m) just add an int value (: (\x1b[1;33mnumber\x1b[1;37m)")
fileLength = raw_input("\x1b[1;37mEnter Desired FileLength: \x1b[1;36m")
print("\x1b[1;37mToken Input is for your desired SecretKey (\x1b[1;32mthis will make it so only ppl with the key can upload files, it helps ALOT\x1b[1;37m)")
token1 = raw_input("\x1b[1;37mEnter Desired Token: \x1b[1;36m")
token2 = raw_input("\x1b[1;37mEnter Desired Secondary Token: \x1b[1;36m")
print("\x1b[1;37mThis is just for shareX, itll be the display name for the configuration file.")
configName = raw_input("\x1b[1;37mEnter Desired ConfigName: \x1b[1;36m")


outF = open("/var/www/html/upload.php", "w")
textList = [
"<?php",
"header('Content-type:application/json;charset=utf-8');",
"error_reporting(E_ERROR);",
"$tokens = array('"+ token1 +"', '"+ token2 +"');",
"$sharexdir = '"+uploadDir+"/';",
"$lengthofstring = "+fileLength+";",
"function RandomString($length) {",
"    $keys = array_merge(range(0,9), range('a', 'z'));",
"    for($i=0; $i < $length; $i++) {",
"        $key .= $keys[mt_rand(0, count($keys) - 1)];",
"    }",
"    return $key;",
"}",
"if(isset($_POST['secret']))",
"{",
"    if(in_array($_POST['secret'], $tokens))",
"    {",
"        $filename = RandomString($lengthofstring);",
"        $target_file = $_FILES['sharex']['name'];",
"        $fileType = pathinfo($target_file, PATHINFO_EXTENSION);",
"        if (move_uploaded_file($_FILES['sharex']['tmp_name'], $sharexdir.$filename.'.'.$fileType))",
"        {",
"            $json = ['status' => 'OK','errormsg' => '','url' => $filename . '.' . $fileType];",
"        }",
"            else",
"        {",
"           $json = ['status' => 'ERROR','errormsg' => '','url' => 'File upload failed. Does the folder exist and did you CHMOD the folder?'];",
"        }  ",
"    }",
"    else",
"    {"
"        $json = ['status' => 'ERROR','errormsg' => '','url' => 'Invalid secret key.'];",
"    }",
"}",
"else",
"{",
"    $json = ['status' => 'ERROR','errormsg' => '','url' => 'No POST data recieved.'];",
"}",
"echo(json_encode($json));",
"?>"
]
for line in textList:
  print >>outF, line
outF.close()
cri('cd /var/www/html/ && rm -rf '+ uploadDir +'/ && mkdir '+ uploadDir +' && chmod 777 '+ uploadDir +'/ && cd')

cri('clear')
print("\x1b[1;37mfile created in /var/www/html/")
print("\x1b[1;37mbelow you can find the .sxcu (shareX config), simply copy the following text and either save to file or import from clipboard.")

print('\x1b[1;34m{')
print('\x1b[1;34m  "Name": "'+configName+'",')
print('\x1b[1;34m  "DestinationType": "ImageUploader, TextUploader, FileUploader",')
print('\x1b[1;34m  "RequestType": "POST",')
print('\x1b[1;34m  "RequestURL": "http://'+domain+'/upload.php",')
print('\x1b[1;34m  "FileFormName": "sharex",')
print('\x1b[1;34m  "Arguments": {')
print('\x1b[1;34m    "secret": "'+token1+'"')
print('\x1b[1;34m  },')
print('\x1b[1;34m  "ResponseType": "Text",')
print('\x1b[1;34m  "URL": "http://'+domain+'/'+uploadDir+'/$json:url$"')
print('\x1b[1;34m}\x1b[1;37m')
