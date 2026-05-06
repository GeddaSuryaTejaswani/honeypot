import os

# Fake file system
fake_fs = {
    "C:\\Users\\Admin": ["Documents", "Downloads", "passwords.txt"],
    "C:\\Users\\Admin\\Documents": ["report.docx", "notes.txt"],
}

current_dir = "C:\\Users\\Admin"


def emulate_windows_command(command):

    global current_dir

    cmd = command.lower().strip()

    # -------------------
    # NORMAL COMMANDS
    # -------------------

    if cmd == "dir":
        files = fake_fs.get(current_dir, [])
        return f"Directory of {current_dir}\n\n" + "\n".join(files)

    elif cmd.startswith("cd"):
        parts = command.split(" ")

        if len(parts) > 1:
            new_path = current_dir + "\\" + parts[1]

            if new_path in fake_fs:
                current_dir = new_path
                return f"Changed directory to {current_dir}"
            else:
                return "The system cannot find the path specified."

        return current_dir

    elif cmd.startswith("type"):
        return "Fake file content: username=admin password=1234"

    elif cmd == "whoami":
        return "admin-pc\\administrator"

    elif cmd == "ipconfig":
        return """
IPv4 Address : 192.168.1.10
Subnet Mask  : 255.255.255.0
Gateway      : 192.168.1.1
        """

    # -------------------
    # ATTACK SIMULATION
    # -------------------

    elif "powershell" in cmd:
        return "Launching PowerShell...\nBypassing execution policy...\nExploit executed."

    elif "net user" in cmd:
        return "System error 5 has occurred.\nAccess is denied."

    elif "sql" in cmd:
        return "Connecting to database...\nDumping tables...\nSuccess."

    elif "nmap" in cmd:
        return "Scanning network...\nOpen ports: 22, 80, 443"

    elif "hydra" in cmd:
        return "Starting brute force attack...\nPassword found: admin123"

    elif "john" in cmd:
        return "Cracking passwords...\nPassword cracked: 123456"

    # -------------------
    # DEFAULT
    # -------------------

    return "Command executed."