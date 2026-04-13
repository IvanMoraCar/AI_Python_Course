<<<<<<< HEAD
=======
def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

>>>>>>> 05cb132 (Adding all_checks script)
def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
<<<<<<< HEAD
    if check_disk_full(disk="/", min_gb=2, min_percent=10):
        print("Disk full.")
        sys.exit(1)

=======
    if check_root_full():
        print("Root partition full.")
        sys.exit(1)
>>>>>>> 05cb132 (Adding all_checks script)
