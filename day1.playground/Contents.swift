import UIKit
import Foundation

let dirs = NSSearchPathForDirectoriesInDomains(.documentDirectory,.userDomainMask, true)
print(dirs)
//let file = "input.txt" // My change to your code - yours is presumably set off-screen
//if let directories = dirs {
//    let dir = directories[0]; //documents directory
//    let path = dir.stringByAppendingPathComponent(file);
//
//    //read
//    let content = NSString(contentsOfFile: path, usedEncoding: nil, error: nil)
//    // works...
//}
