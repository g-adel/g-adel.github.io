# Script to move generative art files to their new folder structure
# Run this from the root of your Jekyll site

# Move CircPath files
Move-Item -Path "Generative\CircPath_1.png" -Destination "_generative\CircPath\" -Force

# Move Pixels files
Move-Item -Path "Generative\Pixels_1.gif" -Destination "_generative\Pixels\" -Force

# Move Salt files
Move-Item -Path "Generative\Salt_1.png" -Destination "_generative\Salt\" -Force
Move-Item -Path "Generative\Salt_2.mp4" -Destination "_generative\Salt\" -Force
Move-Item -Path "Generative\Salt_3.png" -Destination "_generative\Salt\" -Force

# Move Sand files
Move-Item -Path "Generative\Sand_1.png" -Destination "_generative\Sand\" -Force
Move-Item -Path "Generative\Sand_2.mp4" -Destination "_generative\Sand\" -Force

# Move Sorted files
Move-Item -Path "Generative\Sorted_1.png" -Destination "_generative\Sorted\" -Force

# Move Trails files
Move-Item -Path "Generative\Trails_1.png" -Destination "_generative\Trails\" -Force
Move-Item -Path "Generative\Trails_2.png" -Destination "_generative\Trails\" -Force

# Move Transformations files
Move-Item -Path "Generative\Transformations_1.png" -Destination "_generative\Transformations\" -Force
Move-Item -Path "Generative\Transformations_2.png" -Destination "_generative\Transformations\" -Force
Move-Item -Path "Generative\Transformations_3.mp4" -Destination "_generative\Transformations\" -Force

Write-Host "Files moved successfully!" -ForegroundColor Green
Write-Host "You can now delete the old Generative folder and the old generative-*.md files from the root." -ForegroundColor Yellow
